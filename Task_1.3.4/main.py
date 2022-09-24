x = input('Введите строку\n')


def validate(string: str):
    return string.count('[') == string.count(']') and string.count('(') == string.count(')') and string.count('{') == string.count('}')


print(validate(x))
