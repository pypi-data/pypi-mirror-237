from typing import List

from qwak.inner.build_config.build_config_v1 import BuildConfigV1
from qwak.inner.build_logic.constants.step_description import BuildPhase, PhaseDetails
from qwak.inner.build_logic.interface.context_interface import Context
from qwak.inner.build_logic.trigger_build_context import TriggerBuildContext

from qwak.inner.build_logic.interface.step_inteface import Step
from .phase.a_fetch_model_code import get_fetch_model_code_steps
from .phase.b_remote_register_qwak_build import get_remote_register_qwak_build_steps
from .phase.c_deploy import get_deploy_steps


class StepsPipeline:
    def __init__(
        self,
        config: BuildConfigV1,
        context: Context,
        build_phase: BuildPhase = None,
    ) -> None:
        self._phases: List[StepsPipeline] = []
        self._steps: List[Step] = []
        self.context = context
        self._config = config
        self.build_phase = build_phase

    @property
    def phases(self) -> List["StepsPipeline"]:
        return self._phases

    @property
    def steps(self) -> List[Step]:
        return self._steps

    def add_phase(self, steps: List[Step], build_phase: BuildPhase):
        phase = StepsPipeline(
            config=self._config, context=self.context, build_phase=build_phase
        )

        for step in steps:
            step.context = self.context
            step.config = self._config
            step.build_phase = build_phase
            phase._steps.append(step)

        self._phases.append(phase)

    def get_phase_details(self) -> PhaseDetails:
        return PhaseDetails(self.build_phase)


def remote_build_steps(config: BuildConfigV1) -> StepsPipeline:
    steps_root = StepsPipeline(config=config, context=TriggerBuildContext())
    steps_root.add_phase(
        steps=get_fetch_model_code_steps(),
        build_phase=BuildPhase.FETCHING_MODEL_CODE,
    )
    steps_root.add_phase(
        steps=get_remote_register_qwak_build_steps(),
        build_phase=BuildPhase.REGISTERING_QWAK_BUILD,
    )

    if config.deploy:
        steps_root.add_phase(
            steps=get_deploy_steps(),
            build_phase=BuildPhase.DEPLOY_PHASE,
        )

    return steps_root
