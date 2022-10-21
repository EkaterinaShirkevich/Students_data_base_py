import csv
import querys.crud as c
import os.path

is_exists = os.path.exists('all_students.csv')

def save():
	data = c.get_all()
	with open('all_students.csv', 'w', encoding='utf-8') as file:
		writer = csv.writer(file)
		for value in data:
			writer.writerow(value)
			
	if not is_exists:
		print('\n')
		print('=' * 55)
		print('||', f'Успешный импорт БД.'.center(50), '||')
		print('=' * 55)
	else:
		print('\n')
		print('=' * 55)
		print('||', f'Что-то пошло не так ;)'.center(50), '||')
		print('=' * 55)
	
