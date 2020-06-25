from random import randint
a = [randint(1, 16) for _ in range(20)]
print(a)
k = int(input('Введите индекс элемента который нужно удалить: ')) - 1
for i in range(k + 1, len(a)):
    a[i - 1] = a[i]
a.pop()
print(a)
