import logger_tele as lt
import models as mt

def new_pers():
    data = mt.get_new_per()
    lt.data_per(data)
    
def find_someone():
    user_choice = mt.get_1st_userchar()
    data_persons = lt.get_dictionary_from_file()
    lt.find_in_data(user_choice,data_persons)

     
