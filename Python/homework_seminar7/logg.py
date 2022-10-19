


#записываем новые данные в файл
def data_per(data):
    with open('persons.cvs', 'a', encoding= 'utf-8') as file: #если открывать в excel - не видит символы
        file.write(f'{data}\n')


#получаем актуальные данные из файла в виде словаря
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



# поиск в полученных данных по первой букве
def find_in_data(choice, list1):
   for k,v in list1.items():
       if choice == k[0]:
        print(k,v)


# создаем html версию
def new_create(data):
    
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    for k,v in data.items():
        html += '    <p {}>{} {} </p>\n'\
        .format(style, k,v)
        html += '  </body>\n</html>'
    
    with open('phones.html', 'w', encoding='utf-8') as page:
        page.write(html)

    return data