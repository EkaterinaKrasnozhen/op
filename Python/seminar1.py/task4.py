#Задача 4 Показать первую цифру дробной части числа.
num = float(input())

def float_digit(number):
    num_1 = number//1
    float_num = round(number-num_1,2)
    result = float_num*10
    res = round(result//1)
    print(res)

float_digit(num)