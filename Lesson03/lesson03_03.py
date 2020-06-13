# Power
n = int(input('Enter a positive integer :'))
two_in_power = 2
power = 1
while two_in_power <= n:
    two_in_power *= 2
    power += 1
print('Exponent : ', two_in_power // 2, ',', 'power :', power - 1)
