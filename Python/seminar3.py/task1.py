# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
# time.sleep() задежрка, можно целое указать или float


import time


def rand_time(min, max, index):
    x = time.time_ns()
    ti_me = []
    temp = 0

    for i in range(0, index):
        
            temp = x % 10 + i*i
            if temp > min and temp < max:
                ti_me.append(temp)
                x += x // 10
            temp = x % 100 + i
            if temp > min and temp < max:
                ti_me.append(temp)
                x += x // 100
    return ti_me


print(rand_time(1, 50, 8))

# пользователь вводит диапазон(пока только числа до 100) и количество необходимых значений
# (длину списка)
# как задать длину списка значением index?
