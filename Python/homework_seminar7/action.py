
import mod
import logg

def new_pers():
    data = mod.get_new_per()
    logg.data_per(data)
    

def find_someone():
    user_choice = mod.get_1st_userchar()
    data_persons = logg.get_dictionary_from_file()
    logg.find_in_data(user_choice,data_persons)
    
