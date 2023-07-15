from course_project.api.math.BinaryCode import BinaryCode
from course_project.api.math.multiply.Multiply import Multiply


class ShiftMultipliableLeft(Multiply):
    def multiply(self, multipliable: BinaryCode, multiplier: BinaryCode):
        right_sequence = list()

        multiplier_binary = multiplier.get_direct_code()
        result = BinaryCode(0, 8)

        right_sequence.append(result.get_direct_code())
        right_sequence.append(multipliable.get_direct_code())

        for index in range(multipliable.bitness - 1, 0, -1):
            bit = multiplier_binary[index]

            if bit == '1':
                result += multipliable

            right_sequence.append(result.get_direct_code())

            if index != 0:
                multipliable = multipliable << 1
                right_sequence.append(multipliable.get_direct_code())
        right_sequence.append(result.get_direct_code())

        print(right_sequence)
