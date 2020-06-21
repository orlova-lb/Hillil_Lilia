# пустой треугольник
height = int(input('Please enter the height of figure:\t'))
width = height * 2 - 1

print(' "A"')
for i in range(height):
    for j in range(width):
        if j == height - 1 - i or j == height - 1 + i or i == height - 1:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
print()


# заполненный треугольник
print(' "B"')
for i in range(height):
    for j in range(width):
        if height - 1 - i <= j <= height - 1 + i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
print()



# ромб 1
print(' "C"')
for i in range(height):
    for j in range(width):
        if height - 1 - i <= j <= height - 1 + i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
for i in range(height):
    if i == 0:
        continue
    for j in range(width):
        if i == j or i == width - j - 1:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
print()

# ромб 2
print(' "D"')
for i in range(height):
    for j in range(width):
        if height - 1 - i <= j <= height - 1 + i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
for i in range(height):
    if i == 0:
        continue
    for j in range(width):
        if i == j or i == width - j - 1 or j == width // 2:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
print()
