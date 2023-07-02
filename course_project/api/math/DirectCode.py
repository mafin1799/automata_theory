from BinaryCode import BinaryCode, add_lists_with_carry


class DirectCode(BinaryCode):
    def __init__(self, number, bitness=32):
        bits = None
        if isinstance(number, list):
            bits = number
        elif isinstance(number, DirectCode):
            bits = number.bits
        elif isinstance(number, str):
            bits = [int(bit) for bit in number]
        elif isinstance(number, int):
            if number < 0:
                binary_string = bin(number)[3:]
            else:
                binary_string = bin(number)[2:]
            bits = [int(bit) for bit in binary_string]
        if len(bits) > bitness:
            pass
            #raise ValueError("Переполнение разрядной сетки")
        super().__init__(bits, bitness)

    def __lshift__(self, shift):
        shifted_bits = self.bits + [0] * shift
        return self.__class__(shifted_bits, self.bitness)

    def __rshift__(self, shift):
        shifted_bits = [0] * shift + self.bits
        return self.__class__(shifted_bits, self.bitness)

    def __add__(self, other):
        # Сложение в прямом коде без учета знака
        other_binary = DirectCode(other, self.bitness)
        result = add_lists_with_carry(self.bits, other_binary.bits)
        return DirectCode(result, self.bitness)


binary = DirectCode("001")


binary2 = DirectCode(19, 5)
print(binary)
print(binary2 + binary)
print(bin(8))

