nums = []
num_count = 0
avnum = 0
step = 0

print('Введите путь файла: ')
file = input()

with open(r'' + file + '\\nums.txt', 'r') as test:
    for line in test:
        z = line.strip()
        x = int(z)
        num_count = num_count + 1
        avnum = avnum + int(z)
        nums.append(x)

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



