# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
# time.sleep() задежрка, можно целое указать или float


import time


def rand_time(a, b):
    x = time.time_ns()
    print(x)
    ti_me = []
    if a<10: a = 10
    if 10<a<100: a = 100

    while x > 0:
        ti_me.append(x%10)
        ti_me.append(x%100)
        x = x // 10

    return ti_me


print(rand_time(1, 50))
