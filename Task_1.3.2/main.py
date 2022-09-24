def is_palindrome(string: str):
    s = string.replace(' ', '')
    return s == s[::-1]


print(is_palindrome('abcd'))
print(is_palindrome('taco cat'))
print(is_palindrome('black cat'))
print(is_palindrome('rotator'))
