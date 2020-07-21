"""Необходимо написать функцию которая разворачивает исходный список наоборот.

Алгоритм прост и ваши действи заключаются в следующем: мы меняем местами 0-ый элемент с последним,
1-ый с предпоследним и д.т.

Итого количество таких обменов будет равно половине длины списка. Иначе элементы поменяются местами по-второму
 кругу ивернутся в первоначальное положение.

Применять функцию revers() или срезы с шагом -1 нельзя. Так же, нельзя использовать дополнительные
переменные (можно использовать переменную цикла for) и списки."""

from random import randint


def reverse_list(lst):
    for i in range(0, len(lst)//2):
        lst[i], lst[len(lst)-i] = lst[len(lst)-i], lst[i]


my_list = [randint(0, 100) for _ in range(30)]
print(my_list)
res = reverse_list(my_list)
print(res)