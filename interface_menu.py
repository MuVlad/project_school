from read_data import *
from user_input import *
import search_data

def menu():
    menu = ['1', '2', '3', '4']
    point = None
    while point not in menu:
        print('''
Выбирите интерисующий пункт меню:\n 
1. Список всех учеников
2. Информация по конкретному ученику
3. Добавить ученика
4. Выход
''')
        point = input('Введите цифру: ')
        if point == '1':
            print('\nВесь список студентов:')
            print(read_data())
        elif point == '2':
            request = input('Введите фамилию учиника: ')
            data = read_data()
            student = search_data(request,data)
            if student != None:
                print(student)
            else:
                print('Такой ученик не найден!')
        elif point == '3':
            add_data()
            print('Ученик успешно добавлен!')
        elif point == '4':
            print('До свидания')
            break
        else:
            print('\n--------------------------------------')
            print('Некорректный ввод, попробуйте еще раз!')
            print('--------------------------------------\n')
        point = None

