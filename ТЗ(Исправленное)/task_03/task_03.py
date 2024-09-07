import json

try:
    with open('tests.json', 'r') as tests_file:
        tests_data = json.load(tests_file)
except FileNotFoundError:
    print("Ошибка: Файл 'tests.json' не найден!")
    exit()

try:
    with open('values.json', 'r') as values_file:
        values_data = json.load(values_file)
except FileNotFoundError:
    print("Ошибка: Файл 'values.json' не найден!")
    exit()


values_dict = {item['id']: item['value'] for item in values_data['values']}


def fill_values(tests):
    for test in tests:
        test_id = test['id']
        if test_id in values_dict:
            test['value'] = values_dict[test_id]
        
       
        if 'subtests' in test:
            fill_values(test['subtests'])


fill_values(tests_data['tests'])
    
with open(r'report.json' , 'w') as report_file:
    json.dump(tests_data, report_file, indent = 4)

print('Файл создан успешно!')

