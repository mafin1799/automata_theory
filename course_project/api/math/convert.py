def toDirect(num, range):
    direct_code = format(num, range)
    return direct_code.replace('-','1')

# Обратный код
def toInverse(num, range):
    inverse_code = format(num, range)
    if num < 0:
        inverse_code = ''.join('0' if bit == '1' else '1' for bit in inverse_code)
    return inverse_code


# Дополнительный код
def toComplement(num, range):
    complement_code = int(toInverse(num, range), 2)
    if num < 0:
        complement_code += 1
    return format(complement_code, range)


#Test
print(toDirect(12, '08b'))
print(toInverse(12, '08b'))
print(toComplement(12, '08b'))
