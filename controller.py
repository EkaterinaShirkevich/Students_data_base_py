import user_interface as us_if
import input as inp
import model.add_student as add


# запуск приложения
def run():
	print('=' * 50)
	print('Добро пожаловать в нашу базу данных')
	
	while (True):
		us_if.main_menu()	# основное меню
		i = inp.choice_menu_input(4)	# ввод выбора действия
		
		if i == 1:
			us_if.menu_data_actions()   # меню действий с контактов(создание/удаление)
			i = inp.choice_menu_input(5)	# ввод выбора действия
			if i == 1:
				# log.oper_logger('Создать данные') 
				print('-' * 50)
				print('Вы выбрали "Создать данные"')
				print('-' * 50)
				add.add()
				# создать данные
				
			elif i == 2:
				# log.oper_logger('Изменить данные')
				print('-' * 50)
				print('Вы выбрали "Изменить данные"')
				print('-' * 50)
                
				# Изменить данные
			elif i == 3:
				# log.oper_logger('Удалить данные')
				print('-' * 50)
				print('Вы выбрали "Удалить данные"')
				print('-' * 50)
				# удалить данные
            
			elif i == 4:
				# log.oper_logger('Возврат в главное меню')
				print('-' * 50)
				print("Вернуться в главное меню")
				print('-' * 50)
				continue
			elif i == 5:
				# log.oper_logger('Выход из программы')
				print('-' * 50)
				print("Программа завершила работу")
				print('-' * 50)
				break

		elif i == 2:
			us_if.export_menu()	# меню экспорта контактов из файла
			i = inp.choice_menu_input(5)
			if i == 1:
				# log.oper_logger('Вывод всех данных')
				print('-' * 50)
				print('Вы выбрали "Вывод всех данных"')
				print('-' * 50)
				# показать все данные
			elif i == 2:
				# log.oper_logger('Вывод информации о контакте')
				print('-' * 50)
				print('Вы выбрали "Вывод данных по указанным фамилии и имени"')
				print('-' * 50)
				# показать отдельно взятый контакт по имени и фамилии
			
			elif i == 3:
				# log.oper_logger('Вывод информации о контакте')
				print('-' * 50)
				print('Вы выбрали "Вывод данных о классе"')
				print('-' * 50)
				# показать отдельно класс
			
			elif i == 4:
				# log.oper_logger('Возврат в главное меню')
				print('-' * 50)
				print("Вернуться в главное меню")
				print('-' * 50)
				continue
			elif i == 5:
				# log.oper_logger('Выход из программы')
				print('-' * 50)
				print("Программа завершила работу")
				print('-' * 50)
				break

		elif i == 3:
			us_if.import_menu()	# меню импорта в .csv формат
			i = inp.choice_menu_input(3)
			if i == 1:
				# log.oper_logger('Импорт в файл')
				print('-' * 50)
				print('Вы выбрали "Импортировать в файл"')
				print('-' * 50)
				
				
			
			elif i == 2:
				# log.oper_logger('Возврат в главное меню')
				print('-' * 50)
				print("Вернуться в главное меню")
				print('-' * 50)
				continue
			
			elif i == 3:
				# log.oper_logger('Выход из программы')
				print('-' * 50)
				print("Программа завершила работу")
				print('-' * 50)
				break
				
				
		
		elif i == 4:
			# log.oper_logger('Выход из программы')
			print('-'*50)
			print("Программа завершила работу")
			print('-'*50)
			break

run()