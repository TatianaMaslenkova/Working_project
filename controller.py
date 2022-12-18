import check as ch
import create as cr
import delete as de
import find as fd
import read as rd
import update as up
import interface as ie

def question_cr():
    while True:
        question = ie.question_to_add()
        if question == 'Y':
            cr.record_in_book()
        else:
            break

def question_up():
    while True:
        question = ie.question_to_add()
        if question == 'Y':
            ie.menu_item_options()
            option = ie.menu_item()
            return option
        else:
            break

ie.hello()

while True:
    ie.main_menu()
    n = ie.menu_item()
    if n == 1:
        cr.record_in_book()
        question_cr()
    elif n == 2:
        result = fd.search_contact_by_surname()
        ie.result_search()
        ie.top_line()
        print(result)
    elif n == 3:
        result = fd.search_contact_by_name()
        ie.result_search()
        ie.top_line()
        print(result)
    elif n == 4:
        result = fd.search_contact_by_phone_num()
        ie.result_search()
        ie.top_line()
        print(result)
    elif n == 5:
        ie.result_read()
        rd.Read_csvfile('data.csv')
    elif n == 6:
        while True:
            ie.menu_item_options()
            option = ie.menu_item()
            if option == 1:
                surname = fd.search_contact_by_surname() # возвращаем строку с искомой фамилией
                ie.result_search()
                ie.top_line()
                print(surname)
                up.function_update(surname, name_data_list = 'data.csv')
                question_up()
            elif option == 2:
                name = fd.search_contact_by_name()
                ie.result_search()
                ie.top_line()
                print(name)
                up.function_update(name, name_data_list = 'data.csv')
                question_up()
            elif option == 3:
                tel_num = fd.search_contact_by_phone_num()
                ie.result_search()
                ie.top_line()
                print(tel_num)
                up.function_update(tel_num, name_data_list = 'data.csv')
                question_up()
            else:
                ie.error_menu_item()
    elif n == 7:
        while True:
            ie.menu_item_options()
            option = ie.menu_item()
            if option == 1:
                surname = ch.Check_surname()
                de.delete_contact(surname,name_data_list="data.csv")
            elif option == 2:
                name = ch.Check_name()
                de.delete_contact(name,name_data_list="data.csv")
            elif option == 3:
                tel_num = ch.Check_telephon_number()
                de.delete_contact(tel_num,name_data_list="data.csv")
            else:
                ie.error_menu_item()
    elif n == 8:
        ie.bye()
        break
    else:
        ie.error_menu_item()
