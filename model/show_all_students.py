import data_provider.stdn_manager as st_m
import querys.crud


def show_all_info():
	stdn_list = crud.get_all()
	print('\n')
	print('=' * 72)
	print('||', 'фамилия'.center(10),  '||', 'имя'.center(10), '||', 'возраст'.center(10), '||', 'класс'.center(10), '||', 'статус'.center(10), '||')
	print('=' * 72)
	for stdn in stdn_list:
		print('||', stdn[1].center(10),  '||', stdn[2].center(10), '||', str(stdn[3]).center(10), '||', str(stdn[0]).center(10), '||', stdn[4].center(10), '||')
	print('=' * 72)
