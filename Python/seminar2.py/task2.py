# 2.Для натурального n создать список, состоящий из элементов последовательности 3n + 1.
#     Пример:
#     - Для n = 6: [4, 7, 10, 13, 16, 19]



num = int(input('Введите натуральное число '))

def n_elements(n):
    result = []
    for i in range(1,n+1):
        res = 3*i+1
        result.append(res)
    print (result[:]) # если поставить (*result[:]) то будет печать без [] и ,
# print(result, sep=',') печатаем с разделителем ,
n_elements(num)