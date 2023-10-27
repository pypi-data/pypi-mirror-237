from typing import Tuple

from qwak.exceptions import QuietError
from qwak.inner.build_config.build_config_v1 import BuildConfigV1
from qwak.inner.build_logic.interface.build_logger_interface import BuildLogger
from qwak.inner.build_logic.interface.context_interface import Context

from qwak_sdk.exceptions import QwakGeneralBuildException
from qwak_sdk.exceptions.qwak_remote_build_failed import QwakRemoteBuildFailedException
from .build_run_handlers import BuildRunHandler, CLIBuildRunner, ProgrammaticBuildRunner
from .logger import get_build_logger
from .messages import SUCCESS_MSG_REMOTE, SUCCESS_MSG_REMOTE_WITH_DEPLOY
from .trigger_build_logger import TriggerBuildLogger
from .spinner import spinner
from .time_source import Stopwatch, SystemClockTimeSource, TimeSource
from .utils import zip_logs
from ..build_steps import StepsPipeline, remote_build_steps


def execute_build_pipeline(
    config: BuildConfigV1,
    json_logs: bool,
    programmatic: bool = False,
    use_git_credentials: str = None,
    id_only: bool = False,
):
    with get_build_logger(config=config, json_logs=json_logs) as (
        logger,
        log_path,
    ):
        pipeline, success_msg = create_pipeline(config)
        if use_git_credentials:
            pipeline.context.git_credentials = use_git_credentials
        time_source = SystemClockTimeSource()
        for phase in pipeline.phases:
            phase_details = phase.get_phase_details()
            build_logger = TriggerBuildLogger(
                logger,
                prefix="" if json_logs else phase_details.get_description(),
                phase_details=phase_details,
            )

            if programmatic:
                build_runner = ProgrammaticBuildRunner()
                phase_run(phase, pipeline.context, build_runner, build_logger, time_source)
            else:
                with spinner(
                    text=phase_details.get_description(),
                    show=(config.verbose == 0 and not json_logs),
                ) as sp:
                    build_logger.set_spinner(sp)
                    build_runner = CLIBuildRunner(sp, log_path)
                    phase_run(
                        phase, pipeline.context, build_runner, build_logger, time_source
                    )

    if id_only:
        print(pipeline.context.build_id)
    else:
        print(
            success_msg.format(
                build_id=pipeline.context.build_id,
                model_id=pipeline.context.model_id,
                project_uuid=pipeline.context.project_uuid,
            )
        )
    zip_logs(log_path=log_path, build_id=pipeline.context.build_id)

    return pipeline.context.build_id


def phase_run(
    phase: StepsPipeline,
    context: Context,
    build_runner: BuildRunHandler,
    build_logger: BuildLogger,
    time_source: TimeSource,
):
    build_id = context.build_id
    current_step_phase = None
    stop_watch = Stopwatch(time_source)
    try:
        for step in phase.steps:
            current_step_phase = str(step.build_phase)
            step.set_logger(build_logger)
            build_runner.handle_phase_in_progress(current_step_phase)

            step.execute()

        phase_duration = stop_watch.elapsed_time_in_seconds()
        build_runner.handle_phase_finished_successfully(
            current_step_phase, phase_duration
        )
    except QwakGeneralBuildException as e:
        phase_duration = stop_watch.elapsed_time_in_seconds()
        build_runner.handle_contact_support_error(
            build_id, current_step_phase, e, phase_duration
        )
    except QwakRemoteBuildFailedException as e:
        phase_duration = stop_watch.elapsed_time_in_seconds()
        build_runner.handle_remote_build_error(
            build_id, current_step_phase, e, phase_duration
        )
    except KeyboardInterrupt:
        phase_duration = stop_watch.elapsed_time_in_seconds()
        build_runner.handle_keyboard_interrupt(
            build_id, current_step_phase, phase_duration
        )
    except BaseException as e:
        build_logger.exception("Failed", e)
        phase_duration = stop_watch.elapsed_time_in_seconds()
        if not isinstance(e, QuietError):
            build_runner.handle_pipeline_exception(
                build_id, current_step_phase, e, phase_duration
            )
        else:
            build_runner.handle_pipeline_quiet_exception(
                build_id, current_step_phase, e, phase_duration
            )


def create_pipeline(
    config: BuildConfigV1,
) -> Tuple[StepsPipeline, str]:
    success_message = (
        SUCCESS_MSG_REMOTE_WITH_DEPLOY if config.deploy else SUCCESS_MSG_REMOTE
    )
    pipeline = remote_build_steps(config)

    return pipeline, success_message
