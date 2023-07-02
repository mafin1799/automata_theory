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
    def __init__(self, bits, bits_width):
        self.bits = bits
        self.bits_width = bits_width

    def __str__(self):
        if len(self.bits) > self.bits_width:
            bit_str = ''.join(str(bit) for bit in self.bits)
            return '!' + bit_str
        return ''.join(str(bit) for bit in self.bits)

    def is_negative(self):
        return self.bits[0] == 1
