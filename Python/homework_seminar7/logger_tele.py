

# получаем актуальный список абонентов в словаре

dict = dict()
def get_dictionary_from_file():
  data = open('persons.cvs', 'r', encoding='utf-8')
  file = data.read().replace("{","").replace("}","").replace("'","").split("\n")[:-1]
  data.close
                
  for item in file:
    key = item.split(':')[0]
    value = item.split(':')[1]
    dict[key] = value
    data.close()
  return dict


# вносим новые данные

def data_per(data):
    with open('persons.cvs', 'a') as file:
        file.write(f'{data}\n')


#найти по первой букве абонента в словаре
       
def find_in_data(choice, list1):
   for k,v in list1.items():
       if choice == k[0]:
        print(k,v) 