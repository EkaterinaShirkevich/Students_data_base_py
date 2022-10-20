import sqlite3
import os.path

db_path = "stdn.db"
db_schema = "querys/stdn_schema.sql"
db_is_exists = os.path.exists("stdn.db")

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


def add_stdn_sql(stdn_list):
	with sqlite3.connect(db_path) as db:
		cursor = db.cursor()
		cursor.execute("""INSERT INTO students(
			class_desc, name, surname, age, status_perf) 
			VALUES (?, ?, ?, ?, ?);""", stdn_list)


def stdn_update(stdn_list):
	with sqlite3.connect(db_path) as db:
		cursor = db.cursor()
		#cursor.execute()
		

def get_id(name, surname, class_desc):
	with sqlite3.connect(db_path) as db:
		cursor = db.cursor()
		cursor.execute('''
			select id from students 
			where name= :name and 
			surname= :surname and 
			class_desc = :class_desc''')
			

def get_one():
	with sqlite3.connect(db_path) as db:
		cursor = db.cursor()
		cursor.execute('select class_desc, name, surname, age, status_perf from students')
		return cursor.fetchall()
		
def get_all():
	with sqlite3.connect(db_path) as db:
		cursor = db.cursor()
		cursor.execute('select class_desc, name, surname, age, status_perf from students')
		return cursor.fetchall()
