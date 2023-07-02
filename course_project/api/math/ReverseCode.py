from BinaryCode import BinaryCode, add_lists_with_carry


class ReverseCode(BinaryCode):
    def __init__(self, input_data, bit_width=4):
        if isinstance(input_data, list):
            bits = [1 if bit == 0 else 0 for bit in input_data]
        elif isinstance(input_data, ReverseCode):
            bits = input_data.bits
        elif isinstance(input_data, str):
            bits = [int(bit) for bit in input_data]
            self.sign = bits[0]
            bits = [1 if bit == 0 else 0 for bit in bits]
        elif isinstance(input_data, int):
            if input_data > 0:
                self.sign = 0
                bit_list = [int(bit) for bit in bin(input_data)[2:]]
            elif input_data < 0:
                self.sign = 1
                bit_str = ''.join('1' if bit == '0' else '0' for bit in bin(input_data)[3:])
                bit_list = [int(bit) for bit in bit_str]
            bits = bit_list
        super().__init__(bits, bit_width)

    def __lshift__(self, shift):
        shifted_bits = self.bits + [0] * shift
        return self.__class__(shifted_bits, self.bits_width)

    def __rshift__(self, shift):
        shifted_bits = [0] * shift + self.bits
        return self.__class__(shifted_bits, self.bits_width)


rev = ReverseCode(-10)

print(rev)
