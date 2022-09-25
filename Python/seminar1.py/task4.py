#Задача 4 Показать первую цифру дробной части числа.
num = float(input())

def float_digit(number):
    num_1 = number//1 # можно int(number) до целого числа
    float_num = round(number-num_1,2)
    result = float_num*10
    res = round(result//1)
    print(res)

float_digit(num)

# n = input()
# n_list = n.split('.') - разделяем по точке
# print(n_list[1][0]) печатаем с индексом 1 (второе значение 0,1...) и только один символ