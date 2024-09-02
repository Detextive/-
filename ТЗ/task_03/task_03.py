import json

print('Введите путь файла: ')
file = input()

with open(r'' + file + '\\tests.json', 'r') as tests_file:
    tests_data = json.load(tests_file)

with open(r'' + file + '\\values.json', 'r') as values_file:
    values_data = json.load(values_file)

for 

    


with open(r'' + file + '\\report.json' , 'w') as report_file:
    json.dump(tests_data, report_file)

