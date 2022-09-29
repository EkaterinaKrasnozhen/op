# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
numbers = input('Введите вещественное число ').replace('.', '').replace(',', '')

def sum_float(num):
    sum = 0
    for i in num:
        sum += int(i)
    print(sum)

sum_float(numbers)
