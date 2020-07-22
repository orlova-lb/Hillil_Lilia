""""Дан словарь (смотрите пример ниже) ключами которого являются английские слова,
а значениями - списки латинских слов. Необходимо развеннуть словарь.
Другими словани, необходимо, на основании заданного словаря, создать новый словарь,
у которого в качестве ключей будут взяты латинские слова, из исходного словаря, а значениями будет список,
соответствующих им, английских слов.

Исходный словарь:
d = {
   'apple': ['malum', 'pomum', 'popula'],
   'fruit': ['baca', 'bacca', 'popum'],
   'punishment': ['malum', 'multa']
}"""
dict1 = {
         'apple': ['malum', 'pomum', 'popula'],
         'fruit': ['baca', 'bacca', 'popum'],
         'punishment': ['malum', 'multa']
    }

dict2 = dict()

for i in dict1:
    for k in dict1[i]:
        if k not in dict2:
            emptylist = []
            dict2[k] = emptylist
        dict2[k].append(i)
print(dict2)

