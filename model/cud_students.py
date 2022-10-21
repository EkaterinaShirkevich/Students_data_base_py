from querys import crud
from data_provider import user_input as us_in



# Метод, добавляет ученика в БД.
def add():
    stdn = us_in.input_data() # ввод данных пользователя
    try:
        crud.exec_cud(crud.create, stdn) # метод выполняющий запрос к БД, в параметры передаем запрос и кортеж вводимых значений
        stdn_list = crud.get_all() # метод выполняющий запрос к БД и возвращает результат в виде списка
        print('\n')
    except:
        print('Что-то пошло не так... Возможно проблемы с БД.')


    print('=' * 58)
    print('||', 'фамилия'.center(10), '||', 'имя'.center(10), '||', 'класс'.center(10), '||', 'статус'.center(10), '||')
    print('=' * 58)
    print('||', stdn_list[-1][1].center(10), '||', stdn_list[-1][2].center(10), '||', str(stdn_list[-1][0]).center(10),
          '||', stdn_list[-1][4].center(10), '||')
    print('=' * 58)
    print('||', "Ученик успешно добавлен.".center(10), '||')

# метод удаляет ученика из БД
def del_stdn():
    name = us_in.check_input_string('имя') # ввод данных и проверка ввода
    surname = us_in.check_input_string('фамилия') # ввод данных и проверка ввода
    class_desc = us_in.check_input_digit('класс', 1, 11) # ввод данных и проверка ввода

    try:
        id = crud.get_id(name, surname, class_desc) # получаем id ученика

        crud.exec_cud(crud.delete, (id,)) # метод выполняющий запрос к БД, в параметры передаем запрос и кортеж вводимых значений

        print('=' * 50)
        print('||', 'фамилия'.center(10), '||', 'имя'.center(10), '||', 'класс '.center(10), ' ||')
        print('=' * 50)
        print('||', name.center(10), '||', surname.center(10), '||', str(class_desc).center(10),
              '||')
        print('=' * 50)
        print('||', "Ученик успешно удален.".center(10), '||')
    except:
        print('=' * 50)
        print('Что-то пошло не так... Возможно такой информации нет в БД.')


# метод изменения данных ученика в БД
def update_stdn():
    name = us_in.check_input_string('имя')
    surname = us_in.check_input_string('фамилия')
    class_desc = us_in.check_input_digit('класс', 1, 11)
    try:
        id = crud.get_id(name, surname, class_desc) # получаем id ученика

        # вводим новые параметры
        new_class_desc = us_in.check_input_digit('новый класс', 1, 11)
        age = us_in.check_input_digit('возраст', 7, 16)
        status = us_in.status('статус ученика')

        crud.exec_cud(crud.update, (new_class_desc, age, status, id)) # метод обновляет данные ученика

        print('=' * 72)
        print('||', 'фамилия'.center(10), '||', 'имя'.center(10), '||', 'класс '.center(10), ' ||')
        print('=' * 72)

        print('||', name.center(10), '||', surname.center(10), '||', str(new_class_desc).center(10),
              '||', age.center(10), '||', status.center(10), '||')
        print('=' * 72)
        print('||', "Данные о ученике успешно изменены.".center(10), '||')

    except:
        print('=' * 50)
        print('Что-то пошло не так... Возможно проблемы с БД.')