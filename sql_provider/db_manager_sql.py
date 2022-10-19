import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "mydatabase.db")


def db_create():
    with sqlite3.connect(db_path) as db:
        cursor = db.cursor()
        cursor.execute(
        """CREATE TABLE students(
        class_desc integer,
        name text, 
        surname text, 
        age integer, 
        status_perf text);""")


#
# db_create()


def add_stdn_sql(stdn_list):
    with sqlite3.connect(db_path) as db:
        cursor = db.cursor()
        cursor.execute("""INSERT INTO students(class_desc, name, surname, age, status_perf) VALUES (?, ?, ?, ?, ?);""", stdn_list)

