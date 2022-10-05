# 1.Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

my_list = [3, 6, 8, 9, 0]


def sum_odd_elem(list1):
    elem_ind = []
    elem = []
    sum = 0
    for i in range(0, len(list1)):
        if i % 2 != 0:
            elem_ind.append(i)
            elem.append(list1[i])
    for i in elem_ind:
        sum += my_list[i]
    print(f'элементы на нечетных позициях {elem}, ответ {sum}')


sum_odd_elem(my_list)
