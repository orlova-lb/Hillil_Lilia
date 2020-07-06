"""
Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True,
если год високосный, и False иначе.
"""

def is_year_leap(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return 'True'
    else:
        return 'False'


year = int(input('Введите год : '))
print(is_year_leap(year))
