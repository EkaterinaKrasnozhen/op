# ввести нового абонента

def get_new_per():
        dic = {input('Введите ФИО:'): input('Введите телефон: ')}
        return dic 


# поиск по первой букве Фамилии

def get_1st_userchar():
    char1 = input('Введите первую букву Фамилии: ')
    return char1

# изменить фио, не читается потом файл после перезаписи в logger
def change_name():
        old_name = input('Введите ФИО, которые нужно изменить: ')
        new_name = input('Введите новые данные ФИО: ')
        return old_name, new_name

exit()
def change_telefon():
        new_telef = input('Введите новый номер телефона: ')
        return new_telef
