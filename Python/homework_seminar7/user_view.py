import logger_tele as lt
import models as mt


# запускаем добавление и запись нового абонента
def new_pers():
    data = mt.get_new_per()
    lt.data_per(data)
    
# запускаем поиск по первой букве в словаре
def find_someone():
    user_choice = mt.get_1st_userchar()
    data_persons = lt.get_dictionary_from_file()
    lt.find_in_data(user_choice,data_persons)

    
exit()
# получаем ключ для изменения из словаря и меняем на новое значение, записываем в persons.cvs
# вот тут при перезаписи файл становится не читаемым и с utf-8 и без
def change_data_name():
    new_data_name = mt.change_name()
    file2 = lt.get_dictionary_from_file()
    file2[new_data_name[1]] = file2.pop(new_data_name[0])    
    with open('persons.cvs', 'w') as file_pers:
        for i,k in file2.items():
         file_pers.write(f'{i} {k}\n')
    return file2

#print(change_data_name())
     
