# chess knight
x_1 = int(input('Enter the horizontally coordinate of the first cell  '))
y_1 = int(input('Enter the vertical coordinate of the first cell : '))
x_2 = int(input('Enter the  horizontally coordinate of the second cell : '))
y_2 = int(input('Enter the vertically second cell coordinate : '))
dx = abs(x_1 - x_2)
dy = abs(y_1 - y_2)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('Yes, a horse can get from the first stand to the second in one move')
else:
    print('No, a horse cannot get from the first stand to the second in one move')
