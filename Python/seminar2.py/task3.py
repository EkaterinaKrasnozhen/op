# 3.Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
a_str = input('Введите строку а : ')
b_str = input('Введите строку b : ')


def coincid(a, b):
    res = a_str.count(b_str)
    return res


print(coincid(a_str, b_str))


def coincid2(a_st, b_st):
    index = 0
    if b_st in a_st:
        index += 1
    return index

print(coincid2(a_str,b_str))
