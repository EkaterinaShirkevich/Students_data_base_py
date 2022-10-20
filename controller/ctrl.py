import data_provider.stdn_manager as st_m
import querys.crud as crud
import model.add_student as a_o
import model.show_all_students as s_a

def run():
	crud.db_create()
	a_o.add()
	s_a.show_all_info()




	

