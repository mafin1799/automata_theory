from BinaryCode import BinaryCode, add_lists_with_carry


class ReverseCode(BinaryCode):
    def __init__(self, number, bitness=4):
        bits = None
        if isinstance(number, list):
            bits = [1 if bit == 0 else 0 for bit in number]
        elif isinstance(number, ReverseCode):
            bits = number.bits
        elif isinstance(number, str):
            bits = [int(bit) for bit in number]
            self.sign = bits[0]
            bits = [1 if bit == 0 else 0 for bit in bits]
        elif isinstance(number, int):
            bit_list = None
            if number > 0:
                self.sign = 0
                bit_list = [int(bit) for bit in bin(number)[2:]]
            elif number < 0:
                self.sign = 1
                bit_str = ''.join('1' if bit == '0' else '0' for bit in bin(number)[3:])
                bit_list = [int(bit) for bit in bit_str]
            bits = [self.sign] + bit_list
        super().__init__(bits, bitness)

    def __lshift__(self, shift):
        shifted_bits = self.bits + [0] * shift
        return self.__class__(shifted_bits, self.bitness)

    def __rshift__(self, shift):
        shifted_bits = [0] * shift + self.bits
        return self.__class__(shifted_bits, self.bitness)

    def __invert__(self):
        inverted_bits = [self.bits[0]] + [0 if bit == 1 else 1 for bit in self.bits[1:]]
        return ReverseCode(inverted_bits)

    def __add__(self, other):
        num1 = self.bits
        num2 = ReverseCode(other).bits
        print(num1)
        print(num2)
        len1 = len(num1)
        len2 = len(num2)

        # Дополнение списков ведущими нулями, если необходимо
        if len1 < len2:
            num1 = [0] * (len2 - len1) + num1
        elif len2 < len1:
            num2 = [0] * (len1 - len2) + num2

        result = []
        carry = 0

        for i in range(len(num1[1:]) - 1, -1, -1):
            bit_sum = num1[i] ^ num2[i] ^ carry
            result.insert(0, bit_sum)
            carry = (num1[i] & num2[i]) | ((num1[i] | num2[i]) & carry)

        # Обработка переноса из старшего разряда
        if carry != 0:
            result.insert(0, carry)

        # Удаление ведущих нулей, если есть
        while len(result) > 1 and result[0] == 0:
            result.pop(0)

        return ReverseCode(result)


rev1 = ReverseCode(-3)
rev2 = ReverseCode(-2)

print(~(rev1 + rev2))
