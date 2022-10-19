
import mod
import logg

# получаем и записываем нового абонента

def new_pers():
    data = mod.get_new_per()
    logg.data_per(data)
    

# поиск и выдача абонента(ов) по первой букве фамилии

def find_someone():
    user_choice = mod.get_1st_userchar()
    data_persons = logg.get_dictionary_from_file()
    logg.find_in_data(user_choice,data_persons)
    

#создаем актуальный файл с абонентами html(все ок видно), а excel русские буквы не видит, куда добавить кодировку?

def get_list_phones():
    lis_phones = logg.get_dictionary_from_file()
    logg.new_create(lis_phones)
    

# изменяем фио и перезаписываем справочник
  
def change_data_name():
    new_data_name = mod.change_name()
    file2 = logg.get_dictionary_from_file()
    file2[new_data_name[1]] = file2.pop(new_data_name[0])
       
    with open('persons.cvs', 'w', encoding='utf-8') as file:
       for key, value in file2.items():
          file.write(f'{key}:{value}\n')
    return file2


# изменяем фио и перезаписываем справочник

def change_data_phone():
    new_data_phone = mod.change_phone()
    file2 = logg.get_dictionary_from_file()
    file2[new_data_phone[0]] = new_data_phone[1]
       
    with open('persons.cvs', 'w', encoding='utf-8') as file:
       for key, value in file2.items():
          file.write(f'{key}:{value}\n')
    return file2
    
