from data_provider import user_input as us_in
import querys.crud as crud


# вывод информации о всех учениках
def show_all_info():
    try:
        stdn_list = crud.get_all()  # метод выполняет запрос к БД и возвращает информацию в виде списка кортежей

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
    except:
        print('=' * 72)
        print('Что-то пошло не так... Возможно такой информации нет в БД.')


# вывод информации по классу
def show_class_by_num():
    class_desc = us_in.check_input_digit('класс', 1, 11)
    try:
        class_list = crud.get_class(
            class_desc)  # метод выполняет запрос к БД и возвращает информацию в виде списка кортежей
    except:
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


# вывод информации о ученике
def show_stdn_info():
    name = us_in.check_input_string('имя')
    surname = us_in.check_input_string('фамилия')
    class_desc = us_in.check_input_digit('класс', 1, 11)

    try:
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
    except:
        print('Что-то пошло не так... Возможно такой информации нет в БД.')
