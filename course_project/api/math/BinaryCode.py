class BinaryCode:
    __overflow = "ПЕРЕПОЛНЕНИЕ"

    def __init__(self, number: int, bitness: int = 8):
        self.number = number
        self.bitness = bitness

    def __add__(self, second_number):
        result = self.number + second_number.number

        return BinaryCode(result, self.bitness)

    def __lshift__(self, shift):
        return self.__class__(self.number << shift, self.bitness)

    def __rshift__(self, shift):
        return self.__class__(self.number >> shift, self.bitness)

    def get_direct_code(self):
        binary = self.__get_binary()
        if self.__is_overflow():
            return self.__overflow

        if self.number >= 0:
            return binary
        else:
            return '-' + binary

    def get_inverse_code(self):
        binary = self.__get_binary()
        if self.__is_overflow():
            return self.__overflow
        if self.number >= 0:
            return binary
        else:
            inverse = ''.join('1' if bit == '0' else '0' for bit in binary)
            return inverse

    def get_complement_code(self):
        binary = self.__get_binary()
        if self.__is_overflow():
            return self.__overflow

        if self.number >= 0:
            return binary
        else:
            complement = bin(int('1' + ''.join('1' if bit == '0' else '0' for bit in binary), 2) + 1)[2:].zfill(8)
            return complement

    def __is_overflow(self):
        binary = self.__get_binary()
        return len(binary) > self.bitness

    def __get_binary(self):
        return bin(abs(self.number))[2:].zfill(self.bitness)


print(BinaryCode(-256, bitness=8).get_direct_code())
print(BinaryCode(-256, bitness=8).get_inverse_code())
print(BinaryCode(-256, bitness=8).get_complement_code())

print(BinaryCode(-255, bitness=8).get_direct_code())
print(BinaryCode(-255, bitness=8).get_inverse_code())
print(BinaryCode(-255, bitness=8).get_complement_code())
