import check as ch
import interface as ie
import log as lg

def record_in_book():

    """
    Функция осуществляет ввод данных от пользователя
    Returns:
    pohone_book - файл с данными
    """
    name = ch.Check_name()
    surname = ch.Check_surname()
    tel_num = ch.Check_telephon_number()
    comment = ch.Check_comment()
    with open('data.csv', 'a', encoding='utf-8') as file:
        data = surname + '|' + name + '|' + tel_num + '|' + comment
        file.write(data + '\n')
        lg.create_log(data, 'log.txt', 'Добавление записи') # функция логирования
        ie.create_success()
        # return data
# здесь еще нужно ссылки на проверки.