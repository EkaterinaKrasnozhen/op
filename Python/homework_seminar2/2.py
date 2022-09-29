# 2. Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

num = int(input('Введите число N '))


def multi_N(n):
    result = [1, ]
    if n == 0:
        print(0)
    else:
        for i in range(2, n+1):
            res = i*result[i-2]
            result.append(res)
        print(result)


multi_N(num)
