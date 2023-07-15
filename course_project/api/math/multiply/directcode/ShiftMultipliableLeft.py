from course_project.api.math.BinaryCode import BinaryCode
from course_project.api.math.multiply.Multiply import Multiply


class ShiftMultipliableLeft(Multiply):
    def multiply(self, multipliable: BinaryCode, multiplier: BinaryCode):
        data = list()

        multiplier_binary = multiplier.get_direct_code()
        result = BinaryCode(0, 8)

        data.append(result.get_direct_code())
        data.append(multipliable.get_direct_code())

        for index in range(multipliable.bitness - 1, 0, -1):
            bit = multiplier_binary[index]

            if bit == '1':
                result += multipliable

            data.append(result.get_direct_code())

            if index != 0:
                multipliable = multipliable << 1
                data.append(multipliable.get_direct_code())
        data.append(result.get_direct_code())

        print(data)
