# 4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = 2

def ten_to_double(number):
    double = []
    while number!=0:
         double.append(number%2)
         number//=2
    while double!=0:
        double = double*10+(double%10)
        double//=10
         
    print(double)
    
ten_to_double(num)
