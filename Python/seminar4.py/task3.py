# 3. Задайте два числа. Напишите программу,
# которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

a = int(input("Введите число а: "))
b = int(input("Введите число b: "))


def nok_nums(a1, b1):
    
    for i in range(1, 1000):
        if b1 == 0:
            print(a1)
            break
        elif i % a == 0 and i % b == 0:
            print(f" НОК для {a1} и {b1}  = {i}")  
            break


nok_nums(a, b)

# def nod(a,b):
#   if b == 0:
#     return a
#   else:
#     return nod(b, a % b)

# def nok(a,b):
# return int(abs(a*b)/nod(a,b))