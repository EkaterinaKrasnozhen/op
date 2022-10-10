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

f = open('f.txt', 'r')
data = f.read() + ' '
f.close()

numbers = []

while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos+1:]
    
out = []
for e in numbers:
    if not e%2:
        out.append((e,e**2))
print(out)