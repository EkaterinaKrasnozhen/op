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

# import task_example as te # присовить сокращенное название
# print(te.f(1))

# функции

# def new_string(symbol, count = 3):
#     return symbol*count

# print(new_string('&', 5))
# print(new_string('&'))
# print(new_string(5))

# функции с неограниченным набором аргументов

# def concatenario(*params):
#     res: str = '' # для чисел можно res: int = 0 или просто res = 0
#     for item in params:
#         res+= item
#     return res

# print(concatenario('a', 'b', 'c','d'))
# print(concatenario('a','1'))
# # print(concatenario(1,2,3))

# рекурсия

# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)

# list = []
# for e in range (1,10):
#     list.append(fib(e))

# print(list)

# кортежи (неизменяеимые элементы)

# a = (3,4)
# print(a)
# print(a[0]) # кортеж из одного элемента пишем a = (3,)

# t = tuple(["red", "green", "blue"])
# red, green, blue = t
# print('r{}, g{}, b{}'.format(red,green,blue))

# словари



dictionary = {}
dictionary = \
    {
        'up':'↑',
        'left':'←',
        'down':'↓',
        'right':'→'   
    }
# print(dictionary)
# print(dictionary['left'])

# for k in dictionary.keys(): # печатаем ключи
#     print(k)

# for k in dictionary.values(): # печатаем значения
#     print(k)
    
# for v in dictionary:     # тоже значения
#     print(dictionary[v])
    
# dictionary['left'] = '←'
# print(dictionary['left'])

# # del dictionary['left'] # удаление элемента

# for item in dictionary:      # for (k,v) in dictionary.items()
#     print('{} : {}'.format(item, dictionary[item]))

#множества

# colors = {'red', 'green','blue'} #set тип множества
# colors.add('grey')
# print(colors) # добавит вперед списка
# colors.remove('red') # удалить элемент
# print(colors)
# colors.clear() #очистить все

a = {'grey','e','red'}
b = {'12','done','e', '123'}
# c = a.copy()
# print(c)
# u = a.union(b)
# print(u)
# i = a.intersection(b)
# print(i)
# dl = a.difference(b)
# print(dl)

# q = a\
#     .union(b)\
#     .difference(a.intersection(b)) # объединить и вывести разные элементы
# print(q)

# s = frozenset(a) #сделать неизменяемый

# списки

list1 = [1,2,3,4]
# list2 = list1
# print(list1)
# print()
# print(list2)
# list1[0] = 123
# print(list1)
# print()
# print(list2)  # значения меняются в обоих списках, даже если изменить в list2

print(list1)
print(list1.pop()) #удалеяет последний элемент
print(list1)
print(list1.pop(0)) # удалить конкретный элемент
print(list1.insert(1,11))
print(list1)
print(list1.append(11)) #добавление в конец
print(list1)