from write_data import *
def add_data():
    students = {}
    students['surname'] = input('Введите Фамилию: ')
    students['name'] = input('Введите Имя: ')
    students['hb'] = input('Введите дату рождения(формат: дд.мм.гггг): ')
    students['class'] = input('Введите Класс: ')
    students['status'] = input('Введите Статус: ') #успеваемость

    write_data([students.get('surname'), students.get('name'), students.get('hb'),
                students.get('class'), students.get('status')], 'student_repo.csv')
