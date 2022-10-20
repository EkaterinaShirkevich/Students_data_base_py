import data_provider.stdn_manager as st_m

def add():
	st_m.add_stdn()
	print('\n')
	print('=' * 61)
	print('||', 'фамилия'.center(15),  '||', 'имя'.center(15), '||', 'класс '.center(15), ' ||')
	print('=' * 61)
	print('||', stdn[1].center(15),  '||', stdn[2].center(15), '||', str(stdn[0]).center(15), '||')
	print('=' * 61)
