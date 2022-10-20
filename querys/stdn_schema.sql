CREATE TABLE IF NOT EXISTS students(
			id integer primary key autoincrement not null,
			class_desc integer not null,
			name text not null, 
			surname text not null, 
			age integer not null, 
			status_perf text not null);
