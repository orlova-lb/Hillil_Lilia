"""Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция,
 которая должна быть произведена над ними. Функция должна вернуть результат вычислений зависящий
 от третьего аргумент +, сложить их; если -, то вычесть; * — умножить; / — разделить
 (первое на второе). В остальных случаях вернуть строку "Неизвестная операция"."""


def arithmetic(x, y, z):
    if z == "+":
        return (x + y)
    elif z == "-":
        return (x - y)
    elif z == "*":
        return (x * y)
    elif z == "/":
        return (x / y)
    else:
        return "Неизвестная операция"


x = int(input('Введите первое число : '))
y = int(input('Введите второе чиcло : '))
z = input('Введите операцию : ')
print(arithmetic(x, y, z))
