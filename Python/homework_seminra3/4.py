# 4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


num = 2

def ten_to_double(number):
    double = ""
    temp = number
    while number != 0:

        double = double + str(number % 2)
        number //= 2
        
    # inverted = []
    # for i in range(0, len(double)):
        
    #     inverted.append(double[-1-i])
    
    inverted = ''
    for i in range(0, len(double)):
        inverted = inverted + str(double[-1-i])   

    print(f'{temp} -> {inverted}')

ten_to_double(num)
