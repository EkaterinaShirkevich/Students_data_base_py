import data_provider.stdn_manager as st_m
import querys.crud
import model.add_one as a_o
import model.show_all as s_a

def run():
	crud.db_create()
	a_o.add()
	s_a.show_all_info()
	

