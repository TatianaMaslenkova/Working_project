import interface as ie

def Check_telephon_number(): 
    """Проверка номера телефона"""
    while True:
        tel_num = ie.get_tel_num()
        if tel_num.isdigit() and len(tel_num)==11:
            return tel_num
        else:
            ie.error_tel_num()
            # return False 


def Check_name():
    """Проверка имени"""
    while True:
        name = ie.get_name()
        if name.isalpha() and 2 <= len(name) <= 40:
            return name
        else:
            ie.error_name()
            # return False 

def Check_surname():
    """Проверка фамилии"""
    while True:
        surname = ie.get_surname()
        if surname.isalpha() and 2 <= len(surname) <= 40:
            return surname
        else:
            ie.error_surname()
            # return False 

def Check_comment(): 
    """Проверка комментария"""
    while True:
        comment = ie.get_comment()
        if 2 <= len(comment) <= 301:
            return comment
        else:
            ie.error_comment()
            # return False

# проверки новых данных - нужны новые, т.к. из интерфейса вызываются другие функции (для овых данных)
def Check_new_telephon_number(): 
    """Проверка нового номера телефона"""
    while True:
        new_tel_num = ie.get_new_tel_num()
        if new_tel_num.isdigit() and len(new_tel_num)==11:
            return new_tel_num
        else:
            ie.error_tel_num()
            # return False 


def Check_new_name():
    """Проверка нового имени"""
    while True:
        new_name = ie.get_new_name()
        if new_name.isalpha() and 2 <= len(new_name) <= 40:
            return new_name
        else:
            ie.error_name()
            # return False 

def Check_new_surname():
    """Проверка новой фамилии"""
    while True:
        new_surname = ie.get_new_surname()
        if new_surname.isalpha() and 2 <= len(new_surname) <= 40:
            return new_surname
        else:
            ie.error_surname()
            # return False 

def Check_new_comment(): 
    """Проверка нового комментария"""
    while True:
        new_comment = ie.get_new_comment()
        if 2 <= len(new_comment) <= 301:
            return new_comment
        else:
            ie.error_comment()
            # return False