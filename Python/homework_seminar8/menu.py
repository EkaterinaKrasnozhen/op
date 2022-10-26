import modul_sem8 as m

def user_choice():
    
    while True:
        user_choice = input(""" 1 - найти сотрудника по Фамилии\n 2 - найти сотрудника по ID 
 3 - удалить из базы по номеру\n 4 - обновить данные по зарплате\n 5 - распечатать базу сотрудников\n q - выход\n""")
        if user_choice == '1':
            m.find_last_name()
        elif user_choice =='2':
            m.find_id()
        elif user_choice =='3':  
            m.delete_data()
        elif user_choice =='4': 
            m.update_personal()
        elif user_choice =='5':
            m.print_baza()
        elif user_choice == 'q':
            print('выход')
            break
        else:
            print('нет такого пункта меню')
        print()    

user_choice()