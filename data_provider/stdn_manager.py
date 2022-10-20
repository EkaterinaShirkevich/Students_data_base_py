from sqlite3 import Error
import querys.crud as crud
import data_provider.user_input as us_in


def add_stdn():
	stdn = us_in.input_data()
	try:
		crud.add_stdn_sql(stdn)
	except Error:
		print(Error)

def del_stdn():
	return 
	

def update_stdn():
	return 
