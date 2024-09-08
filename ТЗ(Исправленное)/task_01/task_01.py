n = int(input('Введите длину списка (n): '))
m = int(input('Вводите количество ходов (m): '))

array = []
way = range(1 , n+1)


if n <= 0:
    print('Длинна списка должна быть положительным числом!')
elif m <=0:
    print('Количество шагов должно быть положительным числом!')
elif m > n:
    print('Количество шагов не долно превышать длину списка!')
else:   
    for i in range(1, n+1):
        array.append(i)
        
    last_num = int(0)
    result = str()

    while last_num != 1:
        last_num = array[m - 1]    
        result = result + str(array[0])
        array = array[m - 1:] + array[:m]    
        array.pop(n)

    print('Круговой массив: ' , list(way))
    print('Полученный путь: ', result)
