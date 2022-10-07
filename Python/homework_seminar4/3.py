# 3. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.

my_list = [3, 3, 8, 3, 54, 5]


def unic_elem(a):
    index = 0
    while index < len(a):
        for i in a:
            if int(a[index]) == int(i):
                a.pop(index)
                a.remove(i)
                print(a)
            
            else:
                index+1              

    print(a)


unic_elem(my_list)
