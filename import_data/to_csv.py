import csv
import querys.crud as c

# импорт БД в формат .csv
def save():
	data = c.get_all() # метод выполняющий запрос к БД
	with open('all_students.csv', 'w', encoding='cp1251') as file:
		writer = csv.writer(file)
		for value in data:
			writer.writerow(value)
		print('\n')
		print('=' * 55)
		print('||', f'Успешный импорт БД.'.center(50), '||')
		print('=' * 55)