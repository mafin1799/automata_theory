from BinaryCode import BinaryCode, add_lists_with_carry


class DirectCode(BinaryCode):
    def __init__(self, input_data):
        if isinstance(input_data, list):
            bits = input_data
        elif isinstance(input_data, str):
            bits = [int(bit) for bit in input_data]
        elif isinstance(input_data, int):
            binary_string = bin(input_data)[2:]
            bits = [int(bit) for bit in binary_string]
        # Далее определить конвертацию из обратного и дополнительного кода
        else:
            raise ValueError("Invalid input data type")
        super().__init__(bits)

    def __lshift__(self, shift):
        shifted_bits = self.bits + [0] * shift
        return self.__class__(shifted_bits)

    def __rshift__(self, shift):
        shifted_bits = [0] * shift + self.bits
        return self.__class__(shifted_bits)

    def __add__(self, other):
        # Сложение в прямом коде
        if not isinstance(other, BinaryCode):
            raise ValueError("Invalid operand type for addition")

        if not self.is_negative() and not other.is_negative():
            result = add_lists_with_carry(self.bits, other.bits)

            BinaryCode(result)

            return BinaryCode(result)


binary = DirectCode(10)

binary2 = DirectCode(20)
print(binary << 2)
print(add_lists_with_carry(binary.bits, binary2.bits))
