from BinaryCode import BinaryCode, add_lists_with_carry


class DirectCode(BinaryCode):
    def __init__(self, input_data, bits_width=4):
        if isinstance(input_data, list):
            bits = input_data
        elif isinstance(input_data, DirectCode):
            bits = input_data.bits
        elif isinstance(input_data, str):
            bits = [int(bit) for bit in input_data]
        elif isinstance(input_data, int):
            if input_data < 0:
                self.sign = 1
                print(1)
                binary_string = bin(input_data)[3:]
            elif input_data > 0:
                self.sign = 0
                binary_string = bin(input_data)[2:]
            bits = [int(bit) for bit in binary_string]
        super().__init__(bits, bits_width)

    def __lshift__(self, shift):
        shifted_bits = self.bits + [0] * shift
        return self.__class__(shifted_bits, self.bits_width)

    def __rshift__(self, shift):
        shifted_bits = [0] * shift + self.bits
        return self.__class__(shifted_bits, self.bits_width)

    def __add__(self, other):
        # Сложение в прямом коде без учета знака
        other_binary = DirectCode(other, self.bits_width)
        result = add_lists_with_carry(self.bits, other_binary.bits)
        return DirectCode(result, self.bits_width)


binary = DirectCode("001")

binary2 = DirectCode("001")
print(binary2)
print((binary + binary2))
