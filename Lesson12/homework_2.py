"""Создать текстовый файл, записать в него построчно данные,
которые вводит пользователь.
Окончанием ввода пусть служит пустая строка."""

file = open('homework_2.txt', 'w', encoding='utf-8')
while True:
    s = input()
    if s == '':
        break
    else:
        file.write(s+'\n')
file.close()
