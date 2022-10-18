# import mod
# import logg

# если перезаписываю файл после исправления - файл уже не читается, и с utf-8 и без пробовала записывать и читать,
# и если не закоммичено - то вообще ничего не работает во всей программе, хотя не вызываю нигде это действие


# exit() 
# def change_data_name():
#     new_data_name = mod.change_name()
#     file2 = logg.get_dictionary_from_file()
#     file2[new_data_name[1]] = file2.pop(new_data_name[0])    
#     with open('persons.cvs', 'w') as file_pers:
#         for i,k in file2.items():
#          file_pers.write(f'{i} {k}\n')
#     return file2