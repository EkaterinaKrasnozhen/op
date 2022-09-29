# 3. Задать список из n чисел последовательности (1 + 1/n)^n 
# и вывести на экран их сумму.

num = int(input('Введите число N '))

def nums_N(n):
    result = []
    for i in range(1, n+1):
        res = round((1+1/i)**i,2)
        result.append(res)
    print(result)

nums_N(num)