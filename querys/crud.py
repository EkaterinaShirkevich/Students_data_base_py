import sqlite3
import os.path

db_path = "stdn.db"
db_schema = "querys/stdn_schema.sql"
db_is_exists = os.path.exists("stdn.db")

create = "insert into students(class_desc, name, surname, age, status_perf) VALUES (?, ?, ?, ?, ?);"
delete = "delete from students where name = ? and surname = ? and  class_desc = ?"
update = "update students set class_desc = ?, age = ?, status_perf = ? where id = ?"
get_class_info = "select name, surname, age, status_perf from students where class_desc = ?"
get_stdn_id = "select id from students where name = ? and surname = ? and class_desc = ?"
get_stdn_one = "select class_desc, name, surname, age, status_perf from students where id = ?"
get_stdn_all = "select class_desc, name, surname, age, status_perf from students"

def db_create():
	if not db_is_exists:
		with sqlite3.connect(db_path) as db:
			print('Creating students DB')
			with open(db_schema, 'rt') as file: 
				schema = file.read()
			cursor = db.cursor()
			cursor.execute(schema)
	else:
		print("DB 'students' is already exists")


def exec_cud(query, *args):
	with sqlite3.connect(db_path) as db:
		cursor = db.cursor()
		cursor.execute(query, *args)


def get_id(name, surname, class_desc):
	with sqlite3.connect(db_path) as db:
		cursor = db.cursor()
		id = str(cursor.execute(get_stdn_id, (name, surname, class_desc)).fetchone()[0])
		return id
			

def get_one(id):
	with sqlite3.connect(db_path) as db:
		cursor = db.cursor()
		cursor.execute(get_stdn_one, id)
		return cursor.fetchone()
	

def get_class(class_desc):
	with sqlite3.connect(db_path) as db:
		cursor = db.cursor()
		cursor.execute(get_class_info, class_desc)
		return cursor.fetchall()

		
def get_all():
	with sqlite3.connect(db_path) as db:
		cursor = db.cursor()
		cursor.execute(get_stdn_all)
		return cursor.fetchall()
