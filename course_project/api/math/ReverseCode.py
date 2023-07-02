from BinaryCode import BinaryCode, add_lists_with_carry


class ReverseCode(BinaryCode):
    def __init__(self, number, bitness=4):
        if isinstance(number, list):
            bits = [1 if bit == 0 else 0 for bit in number]
        elif isinstance(number, ReverseCode):
            bits = number.bits
        elif isinstance(number, str):
            bits = [int(bit) for bit in number]
            self.sign = bits[0]
            bits = [1 if bit == 0 else 0 for bit in bits]
        elif isinstance(number, int):
            if number > 0:
                self.sign = 0
                bit_list = [int(bit) for bit in bin(number)[2:]]
            elif number < 0:
                self.sign = 1
                bit_str = ''.join('1' if bit == '0' else '0' for bit in bin(number)[3:])
                bit_list = [int(bit) for bit in bit_str]
            bits = bit_list
        super().__init__(bits, bitness)

    def __lshift__(self, shift):
        shifted_bits = self.bits + [0] * shift
        return self.__class__(shifted_bits, self.bitness)

    def __rshift__(self, shift):
        shifted_bits = [0] * shift + self.bits
        return self.__class__(shifted_bits, self.bitness)


rev = ReverseCode(-10)

print(rev)
