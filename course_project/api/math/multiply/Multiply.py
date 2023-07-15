from abc import ABC, abstractmethod
from course_project.api.math.BinaryCode import BinaryCode


class Multiply(ABC):
    def __init__(self, bitness: int = 16):
        self.bitness = bitness
        self._sequence_length = 0

    @abstractmethod
    def multiply(self, number1: BinaryCode, number2: BinaryCode):
        pass

    def get_sequence_length(self):
        return self._sequence_length
