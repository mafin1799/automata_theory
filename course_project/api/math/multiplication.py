def partial_product_sum(X, multiplier):
    # Преобразуем число X в бинарный формат
    X_bin = bin(abs(X))[2:]  # [2:] удаляет префикс "0b"

    # Преобразуем множитель в бинарный формат
    multiplier_bin = bin(multiplier)[2:]  # [2:] удаляет префикс "0b"

    # Обнуляем сумму частичных произведений
    S = 0

    # Анализируем каждый разряд множителя
    for i in range(len(multiplier_bin)):
        # Сдвигаем сумму влево на один разряд
        S = S << 1

        # Анализируем текущий разряд множителя
        if multiplier_bin[i] == '1':
            # Если разряд равен 1, добавляем |X| к сумме
            S += abs(X)

    return S

X = 0  # Число X
multiplier = 13  # Множитель

result = partial_product_sum(X, multiplier)
print(result)
