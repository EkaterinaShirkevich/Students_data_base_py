def choice_menu_input(max_range):
	while(True):
		i = input("Выбрерите один из вариантов работы: ")
		if i.isdigit() and 1 <= int(i) <= max_range:
			return int(i)
		print("Вам надо ввести число")
		# logs.input_logger('Пользователь ввел некорректные данные')