# 3.Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01]

def float_minus(list1):
    num_float = 0
    new_list =[]
    
    for i in list1:
        num_float = round(i - (i//1),2)
        if num_float>0:
         new_list.append(num_float)
    max = new_list[0]
    min = new_list[1]
    for e in new_list:
        if e<min:
            min = e
        if e>max:
            max = e
    print(max-min)
        
        
float_minus(my_list)