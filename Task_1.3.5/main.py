def multiply(x1: str, x2: str):
    res = int(x1, base=2) * int(x2, base=2)
    return bin(res)[2:]


x1, x2 = input('Введите первое двоичное число\n'), input(
    'Введите второе двоичное число\n')

print(multiply(x1, x2))
