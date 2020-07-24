"""
Необходимо создать матрицу (двухмерный список)

М х N. M и N задаёт пользователь с клавиатуры.

Обязательные условия:

матрица создаётся при помощи list comprehension. При создании, список заполняется случайными числами
(используйте генератор случайных чисел)
необходимо посчитать сумму значений каждой строки (функцию sum() использовать НЕЛЬЗЯ).
Сумма выводится напротив соответствующих строк
необходимо посчитать сумму значений каждой колонки (функцию sum() использовать НЕЛЬЗЯ).
Сумма выводится под соответствующей колонкой
можно использовать ТОЛЬКО ОДИН, одномерный, дополнительный список
можно использовать ТОЛЬКО ОДНУ дополнительную переменную
вывод программы ДОЛЖЕН соответствовать примеру ниже (для форматирования вывода,
вам понадобится функция format())
задача считается выполненной ТОЛЬКО при строгом выполнении всех условий.
"""

from random import randrange
m = int(input('Введите количество строк: '))
n = int(input('Введите количество столбцов: '))
matrix = [[randrange(10, 100) for i in range(n)] for k in range(m)]
lst = []
for i in range(n):
    s = 0
    for k in matrix:
        s += k[i]
    lst.append(s)
for i in range(m):
    s = 0
    for k in range(n):
        print('{0: >{1}}'.format(matrix[i][k], len(str(lst[k]))), end=' ')
        s += matrix[i][k]
    print('    ', s)
for i in lst:
    print(i, end=' ')
