# Number
n = int(input('Enter a positive inteser three-digit number :'))
a = n % 10
b = n // 10 % 10
c = n // 100
d = a * 100 + b * 10 + c
print('The number inverse to it ' , d)
