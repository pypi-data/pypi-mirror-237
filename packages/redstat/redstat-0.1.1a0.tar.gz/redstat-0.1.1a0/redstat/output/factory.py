from typing import Type

from redstat.output.base import Output
from redstat.output.classes import ConsoleOutput, FileOutput


class OutputFactory:

    @staticmethod
    def get(output_value) -> Type[Output]:
        if output_value is not None:
            return FileOutput
        return ConsoleOutput
