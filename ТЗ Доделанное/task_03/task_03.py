import json
import argparse
import sys


parser = argparse.ArgumentParser(description='Заполнение тестов значениями из values.json')

parser.add_argument('--tests', type=str, required=True, help='Путь к файлу tests.json')
parser.add_argument('--values', type=str, required=True, help='Путь к файлу values.json')
parser.add_argument('--output', type=str, default='report.json', help='Путь для сохранения выходного файла')


args = parser.parse_args()


try:
    with open(args.tests, 'r') as tests_file:
        tests_data = json.load(tests_file)
except FileNotFoundError:
    print(f"Ошибка: Файл '{args.tests}' не найден!")
    sys.exit()


try:
    with open(args.values, 'r') as values_file:
        values_data = json.load(values_file)
except FileNotFoundError:
    print(f"Ошибка: Файл '{args.values}' не найден!")
    sys.exit()

values_dict = {item['id']: item['value'] for item in values_data['values']}

def fill_values(tests):
    for test in tests:
        test_id = test['id']
        if test_id in values_dict:
            test['value'] = values_dict[test_id]
        
        if 'subtests' in test:
            fill_values(test['subtests'])

fill_values(tests_data['tests'])

with open(args.output, 'w') as report_file:
    json.dump(tests_data, report_file, indent=4)

print(f'Файл {args.output} создан успешно!')
