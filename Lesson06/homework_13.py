from random import randint
a = [randint(1, 16) for _ in range(20)]
print(a)
k = int(input('Введите индекс k :'))
C = int(input('Введите значение C :'))
a.append(0)
for i in range(len(a) - 1, k, -1):
    a[i] = a[i - 1]
a[k - 1] = C
print(' '.join([str(i) for i in a]))
