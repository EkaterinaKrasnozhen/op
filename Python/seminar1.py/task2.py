# Задача 3 Вывести на экран числа от -N до N.
number = -5
def mines_to_plus_num(num):
    number_one = num*-1
    index =0
    if (num>0):
        while (number_one<num):
            print (number_one+index)
            index = 1
            number_one = number_one+index
    if (num<0):
        while (num<number_one):
            print (num+index)
            index =1
            num = num+index         
print(mines_to_plus_num(number))