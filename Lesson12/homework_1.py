"""
 Андрей Говорухи                        6 6 1 4 9 9 10 4 8 2 3 8
 Василий Петров                         2 9 4 7 6 6 3 6 5 5 2 4
 Гавриил Варфаломеев                    10 10 4 10 7 9 4 6 8 1 1 1
 Игнат Тюльпанов                        8 1 4 1 1 5 2 5 2 2 10 8
 Илья Муромцев                          1 6 4 7 10 9 5 3 7 4 7 2
 Кощей Бессмертный                      3 10 1 4 1 8 10 6 2 10 7 4
 Максим Мухин                           10 8 9 9 5 8 6 5 7 2 4 10
 Маргарита Мартынова                    9 1 5 1 10 10 2 4 4 9 8 10
 Петр Николаев                          2 9 5 9 1 2 8 7 8 1 9 1
 Полина Гусева                          9 2 8 7 3 9 9 5 1 9 2 6
 Спиридов Тереньтьев                    4 7 7 3 10 9 7 2 10 9 8 1
 Станислав Трердолобов                  8 1 6 1 4 1 10 8 8 1 8 8
 """

a = open('Source.txt', 'r', encoding='utf-8').readlines()
output = open('Result.txt', 'w', encoding='utf-8')
dict1 = dict()
summa1 = 0
maxlen = 0
for k in range(len(a)):
    a[k] = a[k].split()
    a[k][0] = a[k][0][0] + '.'
    summa = 0
    for i in range(2, len(a[k])):
        summa += int(a[k][i])
    summa = summa/int(len(a[k][2:]))
    summa1 += summa
    print('{: <15}'.format(a[k][1] + ' ' + a[k][0], maxlen),
          '{:.2f}'.format(summa), sep='\t', file=output)
    if summa < 5:
        dict1[a[k][1] + ' ' + a[k][0]] = summa
    if maxlen < len(a[k][1] + ' ' + a[k][0]):
        maxlen = len(a[k][1] + ' ' + a[k][0])

for k in dict1:
    print('{0: <{1}}'.format(k, maxlen), '{:.2f}'.format(dict1[k]), sep='\t')
print('{0: <{1}}'.format('Класс', maxlen), '{:.2f}'.format(summa1 / len(a)),
      sep='\t')
output.close()

