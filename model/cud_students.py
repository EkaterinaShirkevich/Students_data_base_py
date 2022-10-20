from querys import crud
import data_provider.user_input as us_in
from sqlite3 import Error

def add():
	stdn = us_in.input_data()
	try:
		crud.add_stdn_sql(stdn)
		print('\n')
	except Error:
		print(Error)

	stdn_list = crud.get_all()
	print('=' * 50)
	print('||', 'фамилия'.center(10),  '||', 'имя'.center(10), '||', 'класс '.center(10), ' ||')
	print('=' * 50)
	print('||', stdn_list[-1][1].center(10),  '||', stdn_list[-1][2].center(10), '||', str(stdn_list[-1][0]).center(10), '||')
	print('=' * 50)
	print('\n')
	print("Ученик успешно добавлен.".center(10))


def del_stdn():

	return


def update_stdn():
	return