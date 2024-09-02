n = int(input('Введите длину списка (n): '))
m = int(input('Вводите количество ходов (m): '))

array = []

for i in range(1, n+1):
    array.append(i)
    
last_num = int(0)
result = str()

while last_num != 1:
    last_num = array[m - 1]    
    result = result + str(array[0])
    array = array[m - 1:] + array[:m]    
    array.pop(n)

print('Полученный путь: ', result)
