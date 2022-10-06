# 2.Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

my_list = [2, 3, 4, 5, 6]

def mult_elem_list(list1):
    mult = []
    index = 0
    for i in range(0,len(list1)//2):
        mult.append(list1[i]*list1[-1-i]) #math.seil(index/2) округлит в большую сторону math.for в меньшую
    if len(list1)%2!=0:
                mult.append(list1[len(list1)//2]*list1[len(list1)//2])
        
    print(mult)
    
mult_elem_list(my_list)