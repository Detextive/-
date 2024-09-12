n = int(input('Введите длину списка (n): '))
m = int(input('Введите количество шагов (m): '))


if n <= 0:
    print('Длина списка должна быть положительным числом!')
elif m == 0:
    print('Количество шагов не должно быть нулем!')
else:
    array = list(range(1, n + 1))
    result = []

    
    m = m % n
    if m < 0:
        m += n

    start_index = 0

    while array:
        
        result.append(array.pop(start_index))

        if not array:  
            break

        start_index = (start_index + m - 1) % len(array)

    print('Круговой массив:', list(range(1, n + 1)))
    print('Полученный путь:', ''.join(map(str, result)))
