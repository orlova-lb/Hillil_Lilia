"""Написать функцию для перевода десятичного числа в другую систему исчисления (2-36).
Небольшая подсказка. В этой задаче вам может понадобиться:
список
метод `revers()` (или срез [::-1], или вместо `revers()`
использовать `insert()` тогда не придётся разворачивать список),
чтоб развернуть список, метод `join()`
строка `ascii_uppercase` из модуля `string`
(её можно получить если сделать импорт `from string import ascii_uppercase`),
она содержит все буквы латинского алфавита."""

from string import ascii_uppercase


def to_base(s, b):
    res = ""
    while s:
        res += BS[s % b]
        s //= b
    return res[::-1] or "0"


BS = '0123456789' + ascii_uppercase
s = int(input('Введите число, которое необходимо перевести: '))
b = int(input('Введите основание системы исчисления: '))
print(to_base(s, b))
