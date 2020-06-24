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

height = int(input('Please enter the height of figure:\t'))
width = height * 2 - 1
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

height = int(input('Please enter the height of figure:\t'))
height = height if height % 2 != 0 else height + 1
print(' "C"')
for i in range(height):
    for j in range(height):
        if i + j >= height // 2 >= j - i and i <= (height - 1) // 2\
            or i - j == ((height - 1) // 2) or i + j == 3 * (height - 1) // 2:
            print("* ", end='')
        else:
            print("  ", end='')
    print()
print()


height = int(input('Please enter the height of figure:\t')) -1
height = height if height % 2 != 0 else height + 1
print(' "D"')
for i in range(height):
    for j in range(height):
        if i + j >= height // 2 >= j - i and i <= (height - 1) // 2 or\
            i - j == ((height - 1) // 2) or i + j == 3 * (height - 1) // 2\
            or j == height // 2 :
            print("* ", end='')
        else:
            print("  ", end='')
    print()
print()

