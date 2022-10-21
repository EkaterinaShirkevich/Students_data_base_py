from user_interface import interface as us_if, input as inp
from model import cud_students as cud
import model.get_info as g_i
from querys import crud
import import_data.to_csv as t_c

# запуск приложения
def run():
	crud.db_create()
	print('=' * 50)
	print('Добро пожаловать в нашу базу данных')

	while (True):
		us_if.main_menu()	# основное меню
		i = inp.choice_menu_input(4)	# ввод выбора действия

		if i == 1:
			us_if.menu_data_actions()   # меню действий с контактов(создание/удаление)
			i = inp.choice_menu_input(5)	# ввод выбора действия
			if i == 1:
				while(True):
					# log.oper_logger('Создать данные')
					print('-' * 50)
					print('Вы выбрали "Создать данные"')
					print('-' * 50)
					# создать данные
					cud.add()
					us_if.repeat_menu()
					i = inp.choice_menu_input(2)
					if i == 1:
						continue
					elif i == 2:
						break

			elif i == 2:
				while(True):
				    # log.oper_logger('Изменить данные')
					print('-' * 50)
					print('Вы выбрали "Изменить данные"')
					print('-' * 50)
					cud.update_stdn()
					us_if.repeat_menu()
					i = inp.choice_menu_input(2)
					if i == 1:
						continue
					elif i == 2:
						break

			elif i == 3:
				while(True):# log.oper_logger('Удалить данные')
					print('-' * 50)
					print('Вы выбрали "Удалить данные"')
					print('-' * 50)
					cud.del_stdn()
					us_if.repeat_menu()
					i = inp.choice_menu_input(2)
					if i == 1:
						continue
					elif i == 2:
						break

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
				g_i.show_all_info()
			elif i == 2:
				while(True):# log.oper_logger('Вывод информации о контакте')
					print('-' * 50)
					print('Вы выбрали "Вывод данных по указанным фамилии и имени"')
					print('-' * 50)
					# показать отдельно взятый контакт по имени и фамилии
					g_i.show_stdn_info()
					us_if.repeat_menu()
					i = inp.choice_menu_input(2)
					if i == 1:
						continue
					elif i == 2:
						break

			elif i == 3:
				while(True):# log.oper_logger('Вывод информации о контакте')
					print('-' * 50)
					print('Вы выбрали "Вывод данных о классе"')
					print('-' * 50)
					g_i.show_class_by_num()
					# показать отдельно класс
					us_if.repeat_menu()
					i = inp.choice_menu_input(2)
					if i == 1:
						continue
					elif i == 2:
						break
			

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
				t_c.save()


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

# run()
