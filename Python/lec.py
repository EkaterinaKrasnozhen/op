# a=123
# b=1.23
# print(type (a))
# print(type (b))
# # value = None
# value = None
# value = 1233
# print (type (value))
# s = 'hello \n "world' #используем разные типы ковычек, чтобы вывелись в строке. еще можно \' если \n  -переход на новую строку

# print(s)
# print (a,b,s)
# print (a,'-', b,'-', s)
# print ('{} - {} - {}'.format(a,b,s))
# print (f'{a} - {b} - {s}')
# print ('{1} - {2} - {0}'.format(a,b,s))

# f = True
# print(f)
# d = False
# print(d)

# list = [1,2,3]
# print (list)
# l = ['1','2', 'world', 1,2,3,True] #лучше данные одного типа
# print(l)

#пробел ломает питон

# print('Введите а')
# a = int(input()) #если нужны вещестенные (с плав запятой) пишет float
# print('Введите в')
# b = int(input())
# print(a, '+', b, '=', a+b)
# a=+123 #унарный плюс
# b=-231 #унарный минус
# c=a+b #-,+,*,/ - по умолчанию с запятой ответ, если нужно получить целое число //, 
# # % - остаток от деления, ** возведение в степень
# print(c)
# k = 1.334
# t =3
# n = round (k*t,5)
# print (n)

# сокращенные операции
# a = 3
# a += 5 # можно и с другими ариф операциями *- и тд
# print(a)

# a = 1>3
# print(a)
# a = 1>3 and 1>5
# print (a)
# b = 1 == 2 # != не равно
# print (b)
# a= 'qwe' # или a = [1,2]
# b = 'qwe'# или b = [1,2]
# print (a==b)

# a = 1<2<3<10
# print(a)
# func = 1
# T = 4
# x =123
# print (func<T>(x))
# f = 1>2 or 4<6
# print(f)

# f = [1,2,3]
# print(f)
# print(2 in f) # true тк содержится, или можно not 2 in f и тогда отрицание
# is_odd = f[0]%2 ==0
# print(is_odd)
# # или is_odd = not f[0]%2    0 = False; 1 = True

# a = int(input('a = '))
# b = int(input('b = '))
# if a>b:
#     print(a)
# else:
#     print(b)

# Логический оператор
# username = input('введите имя: ')
# if username == 'Катя':
#     print ('Ура, это Катя')
# elif username == 'Мася':
#     print('я так скучала, Мася')
# elif username  == 'Ярик':
#     print ('Ярик - супер')
# else:
#     print('Привет, ', username)

#Цикл
# original = 23
# inverted = 0
# while original !=0:
#     inverted = inverted*10+(original%10)
#     original//=10
# else:
#     print('пожалуй хватит')
# print(inverted)

#конструкция for
# for i in 1,2,3,4,5:
#     print(i**2)
# # или из списка
# list = [1,2,5,4,10]
# for i in list:
#     print(i)

# r = range(10) # от 0 до 9
# for i in r:
#     print (i)

# for i in range(4):
#     print (i)

# for i in range(3, 7): # диапазон
#     print (i)

# for i in range(3, 14, 2): # диапазон и приращение на 2
#     print (i)

# for i in 'qwe,m ass':
#     print (i)

# text = ' молодец огурец'
# print(len(text))
# print('огурец' in text)
# print(text.isdigit()) #является ли текст цифрами
# print(text.islower()) # все ли строчные буквы
# print(text.replace('молодец', 'НЕ молодец'))
# for c in text:
#     print(c)
# # help() и ставить в скобки название функции или метода, чтобы выйти курсор + q

# text = 'шла саша по шосcе'
# # print(text[0])
# # print(text[1])
# # print(text[len(text)-1])
# # print(text[-5])
# # print(text[:]) #печатаем се длину текста
# # print(text[2:6])  # от 2 до 6 символа, не вкл. если от 0 - то можно 0 не писать, по умолч
# # print(text[len(text)-2:]) # от предпоследнего до последнего(по умолч. можно не писать) символа
# # print(text[3:-5])
# # print(text[0:len(text):6]) # из диапазона печатает каждую 6 букву
# text = text[2:9] + text[-5] + text[:2]
# print (text)

#списки
numbers = [1,2,3,4,5]
print(numbers)
ran = range(1,8)
numbers = list(ran) #приведение типа range к типу list
print(numbers)
numbers[0] = 10
print(f'{len(numbers)} len')
print(numbers)
for i in numbers:
    i*=2
    print(i) # печатаем результат умножения
print (numbers)