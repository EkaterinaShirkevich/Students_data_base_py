from logger import logs


# ввод данных пользователем
def input_data():
	class_desc = check_input_digit('класс', 1, 11)
	name = check_input_string('имя')
	surname = check_input_string('фамилия')
	age = check_input_digit('возраст', 7, 16)
	rating_status = status('статус ученика')
	return (class_desc, name, surname, age, rating_status)

# ввод данных и проверка строковых данных(оптимизация кода)
def check_input_string(desc: str):
	while True:
		val = input('Введите данные в поле "{}": '.format(desc))
		if len(val) < 3 or val.isspace() or not val.isalpha():
			print('поле "{}" должно быть больше 3 букв и не пустым.'.format(desc))
			logs.input_logger('Пользователь ввел некорректные данные')
			continue
		return val.capitalize()

# ввод данных и проверка числовых данных(оптимизация кода)
def check_input_digit(desc: str, min_val, max_val):
	while True:
		val = input('Введите данные в поле "{}": '.format(desc))
		if not val.isdigit() or val.isspace() or not min_val <= int(val) <= max_val:
			print('поле "{}" должно быть из цифр, не пустым и в диапозоне от {} до {}.'.format(desc, min_val, max_val))
			logs.input_logger('Пользователь ввел некорректные данные')
			continue
		return val

# ввод данных для меню выбора действий
def choice_menu_input(max_range):
	while(True):
		i = input("Выбрерите один из вариантов работы: ")
		if i.isdigit() and 1 <= i <= max_range:
			return int(i)
		print("Вам надо ввести число")

# выбор статуса ученика
def status(desc: str):
	status_list = ("Отличник", "Хорошист", "Троечник", "Двоечник")


	while (True):
		print(f"""Выберите один из вариантов в значения поле '{desc}':
						5. Отличник
						4. Хорошист
						3. Троечник
						2. Двоечник
						""")
		i = input(">>> ")
		if not i.isdigit() or not (2 <= int(i) <= 5):
			continue
			print("Вам надо ввести число от 2 до 5")

		elif i == "5":
			return status_list[0]
		elif i == "4":
			return status_list[1]
		elif i == "3":
			return status_list[2]
		elif i == "2":
			return status_list[3]