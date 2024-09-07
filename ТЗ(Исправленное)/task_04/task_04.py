nums = []
num_count = 0
avnum = 0
step = 0

try:
    with open(r'numbers.txt', 'r') as test:
        for line in test:
            z = line.strip()
            if z.isdigit() or (z.startswith('-') and z[1:].isdigit()):
                x = int(z)
                num_count = num_count + 1
                avnum += x
                nums.append(x)
            else:
                print(f'Неккоректная строка: {z}')
                
    if num_count == 0:
        print('Файл пуст или не содержит корректных чисел')
    else: 
        avnum = avnum / num_count
        for i in range(len(nums)):
            while int(avnum) != nums[i]:
                if (nums[i] < avnum):
                        nums[i] += 1
                        step += 1
                elif nums[i] > avnum:
                    nums[i] -= 1
                    step += 1
                print(nums)
        
        print('Минимальное количество ходов: ', step)

except FileNotFoundError:
    print('Файл не найден')
except ValueError as e:
    print(f'Ошибка преобразования данных {e}')

