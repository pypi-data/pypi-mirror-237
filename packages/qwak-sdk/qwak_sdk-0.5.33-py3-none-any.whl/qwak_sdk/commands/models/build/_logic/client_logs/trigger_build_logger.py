import logging
from logging import Logger

from qwak.inner.build_logic.constants.step_description import PhaseDetails
from qwak.inner.build_logic.interface.build_logger_interface import BuildLogger
from yaspin.core import Yaspin


class TriggerBuildLogger(BuildLogger):
    def __init__(
        self, logger: Logger, prefix: str, phase_details: PhaseDetails
    ) -> None:
        self.logger = logging.LoggerAdapter(
            logger,
            {
                "phase": phase_details.get_description(),
                "phase_id": phase_details.get_id(),
            },
        )
        self.prefix = f"{prefix} - " if prefix else ""
        self.spinner = None

    def set_spinner(self, spinner: Yaspin):
        self.spinner = spinner

    def exception(self, line: str, e: BaseException) -> None:
        self.logger.error(
            f"""Message: {line}
Exception: {e}
""",
            exc_info=False,
        )

    def error(self, line: str) -> None:
        self.logger.error(f"{self.prefix}{line}")

    def warning(self, line: str) -> None:
        self.logger.warning(f"{self.prefix}{line}")

    def info(self, line: str) -> None:
        self.logger.info(f"{self.prefix}{line}")

    def debug(self, line: str) -> None:
        self.logger.debug(f"{self.prefix}{line}")

    def spinner_text(self, line: str) -> None:
        if self.spinner:
            self.spinner.text = f"{self.prefix}{line}"
