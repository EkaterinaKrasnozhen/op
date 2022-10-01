# Запись в файлы и работа с ними

# colors = ['red','green','blue']
# data = open('file.txt','a') # a - дописывать(не удаляет старую инфу), или будет создан, r - считать из файла (не создает), 
# # w - записывать и создавать (старые данные удаляются), w+ - открывать для записи и читать из него (может и создать), 
# # r+ = открыть для чтения и записать в него (не создает)
# data.writelines(colors) # разделителей не будет
# data.write('\nLine 2\n')
# data.write('Line 3\n')
# data.close()

# exit() #не выполняет код, который под exit написан
# with open('file.txt', 'w') as data:
#     data.write('Line1\n')
#     data.write('Line2\n')
#     # автоматически закрывает после работы, можно без data.close()
    
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# импорт функций

import 1 