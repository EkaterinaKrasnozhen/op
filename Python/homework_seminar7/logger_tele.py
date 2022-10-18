


dict = dict()
def get_dictionary_from_file():
  data = open('persons.cvs', 'r', encoding='utf-8')
  file = data.read().replace("{","").replace("}","").replace("'","").split("\n")[:-1]
                
  for item in file:
    key = item.split(':')[0]
    value = item.split(':')[1]
    dict[key] = value
    data.close()
  return dict


def data_per(data):
    with open('persons.cvs', 'a', encoding='utf-8') as file:
        file.write(f'{data}\n')
        
def find_in_data(choice, list1):
   for k,v in list1.items():
       if choice == k[0]:
        print(k,v) 