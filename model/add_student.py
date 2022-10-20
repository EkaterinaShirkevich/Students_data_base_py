from multiprocessing import Value
import data_provider.stdn_manager as st_m
import sqlite3


def add():
	st_m.add_stdn()
	con = sqlite3.connect
	cur = con.cursor
	stdn = stdn.db
	cur.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?);", stdn)
	con.commit()
	print('\n')
	print('=' * 61)
	print('||', 'фамилия'.center(15),  '||', 'имя'.center(15), '||', 'класс '.center(15), ' ||')
	print('=' * 61)
	print('||', stdn[1].center(15),  '||', stdn[2].center(15), '||', str(stdn[0]).center(15), '||')
	print('=' * 61)
