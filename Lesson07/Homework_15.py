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
