# 3. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.

my_list = [3, 8, 3, 54, 5, 54]


def unic_elem(a):
    b = set(a.copy())
    print(b)


unic_elem(my_list)


def unic_elem_2(b):
    uniq_list = []
    for i in my_list:
        if my_list.count(i) == 1:
            uniq_list.append(i)
    print(uniq_list)


unic_elem_2(my_list)
