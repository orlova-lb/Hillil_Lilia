"""
Написать функцию сортировки двухмерного списка МхМ (матрицы)
Значение М - задаётся пользователем, с клавиатуры. Может быть любым
целым, положительным числом, больше 5.
Функция должна:
1. найти сумму элементов столбцов и отсортировать столбцы по
возрастанию этих сумм
2. отсортировать каждый нечётный столбец по возрастанию значений снизу
вверх, а каждый чётный столбец по возрастанию значений сверху вниз.
Так же, ваша программа должна иметь функцию вывода данного списка
на экран.
 """


from random import randint


def bubble_sort(mat, lst):

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                for k in range(len(mat)):
                    mat[k][j], mat[k][j+1] = mat[k][j+1], mat[k][j]

    for i in range(len(mat[0])):
        if i % 2:
            for k in range(len(mat) - 1):
                for j in range(len(mat) - k - 1):
                    if mat[j][i] > mat[j + 1][i]:
                        mat[j][i], mat[j + 1][i] = mat[j + 1][i], mat[j][i]
        else:
            for k in range(len(mat) - 1):
                for j in range(len(mat) - k - 1):
                    if mat[j][i] < mat[j + 1][i]:
                        mat[j][i], mat[j + 1][i] = mat[j + 1][i], mat[j][i]

    return mat, lst


def print_result(mat, lst):
    for i in range(len(mat)):
        for k in range(len(mat[i])):
            print('{0:>{1}}'.format(str(mat[i][k]), len(str(lst[k]))), end=' ')
        print()
    for k in lst:
        print(k, end=' ')
    print()


m = int(input('Введите размер матрицы М: '))
mat = [[randint(10, 50) for k in range(m)] for i in range(m)]
listSum = [sum(lst) for lst in mat]
print("\nДо сортировки\n")
print_result(mat, listSum)
mat, lst = bubble_sort(mat, listSum)
print("\nПосле сортировки\n")
print_result(mat, listSum)
