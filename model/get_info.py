from data_provider import user_input as us_in
import querys.crud as crud
from sqlite3 import Error


def show_all_info():
    try:
        stdn_list = crud.get_all()
    except Error:
        print('Что-то пошло не так... Возможно такой информации нет в БД.')

    print('\n')
    print('=' * 72)
    print('||', 'фамилия'.center(10), '||', 'имя'.center(10), '||',
          'возраст'.center(10), '||', 'класс'.center(10), '||',
          'статус'.center(10), '||')
    print('=' * 72)
    for stdn in stdn_list:
        print('||', stdn[1].center(10), '||', stdn[2].center(10), '||',
              str(stdn[3]).center(10), '||',
              str(stdn[0]).center(10), '||', stdn[4].center(10), '||')
    print('=' * 72)


def show_class_by_num():
    class_desc = us_in.check_input_digit('класс', 1, 11)
    try:
        class_list = crud.get_class(class_desc)
    except Error:
        print('Что-то пошло не так... Возможно такой информации нет в БД.')

    print('\n')
    print('=' * 60)
    print('||', f'Список учащихся в {class_desc} классе.'.center(50), '||')
    print('=' * 60)
    print('||', 'фамилия'.center(10), '||', 'имя'.center(10), '||',
          'возраст'.center(10), '||', 'статус'.center(10), '||')
    print('=' * 60)
    for stdn in class_list:
        print('||', stdn[0].center(10), '||', stdn[1].center(10), '||',
              str(stdn[2]).center(10), '||', stdn[3].center(10), '||')
    print('=' * 60)


def show_stdn_info():
    name = us_in.check_input_string('имя')
    surname = us_in.check_input_string('фамилия')

    try:
        class_desc = us_in.check_input_digit('класс', 1, 11)
    except Error:
        print('Что-то пошло не так... Возможно такой информации нет в БД.')

    id = crud.get_id(name, surname, class_desc)
    stdn = crud.get_one(id)
    print('\n')
    print('=' * 72)
    print('||', 'фамилия'.center(10), '||', 'имя'.center(10), '||',
          'возраст'.center(10), '||', 'класс'.center(10), '||',
          'статус'.center(10), '||')
    print('=' * 72)
    print('||', stdn[1].center(10), '||', stdn[2].center(10), '||',
          str(stdn[3]).center(10), '||',
          str(stdn[0]).center(10), '||', stdn[4].center(10), '||')
    print('=' * 72)
