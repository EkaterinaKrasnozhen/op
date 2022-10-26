


# user delete with id
def delete_id():
    us_choice = int(input('Введите номер id для удаления: '))   
    return us_choice

#user search id
def search_id():
    uschoice_id = input('Введите номер id для поиска: ')   
    return uschoice_id

# user search surname
def search_surname():
    uschoice_sur_n = input('Введите Фамилию для поиска: ')   
    return uschoice_sur_n

def update_salary():
    uschoice_id = input('Введите id сотрудника ')
    uschoice_salary = (input('Введите новый оклад '))
    return uschoice_id, uschoice_salary