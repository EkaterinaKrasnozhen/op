
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
    
