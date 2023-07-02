def add_lists_with_carry(list1, list2):
    carry = 0
    result = []
    # Обработка списков пока они не закончатся
    while list1 or list2:
        # Получение следующего элемента из каждого списка
        element1 = list1.pop() if list1 else 0
        element2 = list2.pop() if list2 else 0
        # Сложение элементов с учетом переноса
        sum_elements = element1 + element2 + carry
        element = sum_elements % 2
        carry = sum_elements // 2
        # Добавление результата в начало списка
        result.insert(0, element)
    # Если остался перенос, добавляем его в начало списка
    if carry:
        result.insert(0, carry)
    return result


class BinaryCode:
    def __init__(self, bits, bitness):
        self.bits = bits
        self.sign = bits[0]
        self.bitness = bitness
        self.overflow = len(bits) - 1 > bitness

    def __str__(self):
        bit_str = ''.join(str(bit) for bit in self.bits)
        if self.overflow:
            return '!' + bit_str
        return bit_str
