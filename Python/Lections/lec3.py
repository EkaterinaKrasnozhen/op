# функцмм в качестве аргумента

# def f(x):
#     return x**2

# x1=2
# print(type(f))

# g = f
# print(f(x1))
# print(g(x1))

# def calc1(x):
#     return x+10

# def calc2(x):
#     return x*10

# def math1(op,x):
#     print(op(x))

# math1(calc2,10)
# math1(calc1,10)

# def sum(x,y):
#     return x+y


# def mult(x,y):
#     return x*y


# def calc(op, a, b):
#     print(op(a, b))
    # return op(a,b)


# calc(mult,2,3)

# лямбда

# def sum(x,y):
#     return x+y

# sum = lambda x,y: x+y
# calc(sum, 2,2)

# calc(lambda x, y: x + y, 4, 5)

# List Comprehension

# list1 = []
# for i in range(1, 10):
#     if i % 2 == 0:
#         list1.append(i)
# print(list1)

# list2 = [i for i in range(1, 10) if i%2 == 0]
# print(list2)

# list3 = [(i,i) for i in range(1, 10) if i%2 == 0] #создать пару и список кортежей
# print(list3)

#dict comprehension
from random import randint

dict_cmp = {i: randint(0,10) for i in range(10)}
print(dict_cmp)

# def f(x):
#     return x**3
# list4 = [f(i) for i in range(1, 10) if i%2 == 0] #функция f после всех действий возводит в 3 степень
# print(list4)

# list4 = [(i, f(i)) for i in range(1, 10) if i%2 == 0] #тоже самое для наглядности в кортеже
# print(list4)

# def f_2(y):
#     return y*y
# list5 = [(i, f_2(i)) for i in [1,2,3,5,8,15,23,38] if i%2 == 0] # задача с семинара:
# #четные числа из списка возвести в квадрат и записать в кортежи
# print(list5)


#анонимные лямбда функции
# with open("lec3.txt", "a") as data:
#      data.write("1 2 3 5 8 15 23 38")


# path = 'lec3.txt'
# f = open(path, 'r')
# data = f.read() + ' ' #добавляем пробел
# f.close()

# numbers = []

# while data != '':
#     space_pos = data.index(' ') # сохраняем позицию первого пробела
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]
    
# out = []
# for e in numbers:
#     if not e%2:
#         out.append((e,e**2))
# print(out) # программа выполняет задание с лекции: четные значения возвести в квадрат, считывает из файла

# сократить с помощью лямбды
# def select (f,col):
#     return [f(x) for x in col]

# def where (f,col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res  = select(lambda x:(x, x**2), res)
# print(res)

# map
# li = [x for x in range(1,20)]
# li = list(map(lambda x:x+10, li))
# print(li)

# data = list(map(int,input().split())) #по умолчанию разделитель пробел
# print(data)

# data = map(int,'1 2 3 4'.split()) # без приведения к типу list получим итераторы, по ним можно пройтись только один раз
# for e in data:
#     print(e)

# data = '1 2 3 5 8 15 23 38'.split()
# def where (f,col):
#     return [x for x in col if f(x)]
# # убрали функцию select и заменили на map
# res = map(int, data)
# res = where(lambda x: not x % 2, res)
# res  = list(map(lambda x:(x, x**2), res))
# print(res)

# filter (Замена where)

# data = [x for x in range(10)]

# res  = list(filter(lambda x: not x%2, data)) # not x%2 четные, x%2 не четные (тк == 1, true)
# print(res)
# #земенили where на filter
# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = filter(lambda x: not x % 2, res)
# res  = list(map(lambda x:(x, x**2), res))
# print(res)

# zip

# users = ['user1', 'user2', 'user3', 'user5']
# ids = [4,5,9,14,7]
# data = list(zip(users,ids))
# print(data) # сопоставит 1 из users с 1 ids и тд

# users = ['user1', 'user2', 'user3', 'user5']
# ids = [4,5,9,14,7]
# salary = [111,22,33]
# data = list(zip(users,ids, salary)) # сопоставит только для трех первых эелементов из каждого списка
# print(data) # получим кортежи


# enumerate  - на выходе кортежи с пронумерованными элементами

users = ['user1', 'user2', 'user3', 'user5']
ids = [4,5,9,14,7]
salary = [111,22,33]
data = list(enumerate(ids)) # пронумеровать
print(data) # получим кортежи