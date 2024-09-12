import argparse

parser = argparse.ArgumentParser(description='Обработка файла с числами и вычисление среднего значения.')
parser.add_argument('filename', type=str, help='Имя файла с числами')

args = parser.parse_args()


nums = []
num_count = 0
avnum = 0
step = 0


try:
    with open(args.filename, 'w') as file:  
        print("Введите целые числа для записи в файл (введите 'q' для завершения):")
        while True:
            num = input("Введите число: ")
            if num.lower() == 'q':
                break
            if num.isdigit() or (num.startswith('-') and num[1:].isdigit()):                  file.write(num + '\n')
            else:
                print("Некорректное значение. Введите целое число или 'q' для завершения.")
except Exception as e:
    print(f"Ошибка при записи в файл: {e}")

try:
    with open(args.filename, 'r') as test:
        for line in test:
            z = line.strip()
            if z.isdigit() or (z.startswith('-') and z[1:].isdigit()):  
                x = int(z)
                num_count += 1
                avnum += x
                nums.append(x)
            else:
                print(f'Некорректная строка: {z}')

    if num_count == 0:
        print('Файл пуст или не содержит корректных чисел.')
    else:
        avnum = avnum / num_count 
        print(f'Среднее значение: {avnum:.2f}')

        for i in range(len(nums)):
            while int(avnum) != nums[i]:
                if nums[i] < avnum:
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
    print(f'Ошибка преобразования данных: {e}')


