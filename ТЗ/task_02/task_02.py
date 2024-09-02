circle = []
points = []
count = 0

print('Введите путь файла: ')
file = input()

with open(r'' + file + '\\Center.txt', 'r') as file_circle:
    circle = file_circle.read().split()
    for line in file_circle:
        try:
            circle.append(int(line))
        except:
            pass


with open(r'' + file + '\\Points.txt', 'r') as file_points:
    points = file_points.read().split()
    for line in file_points:
        try:
            points.append(int(line))
        except:
            pass


for index in range(int(len(points) / 2)):
    line1 = (float(points[0 + count]) - float(circle[0]) ) ** 2
    line2 = (float(points[1 + count]) - float(circle[1]) ) ** 2
    line = (line1 + line2) ** 0.5
    count += 2
 
    if (line >= float(circle[2])):
        print('2\n')
    elif(line <= float(circle[2])):
         print('1\n')
    else:
         print('0\n')
