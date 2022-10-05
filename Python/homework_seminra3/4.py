# 4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

import string


num = 2

def ten_to_double(number):
    double = ''
    while number!=0:
        
         double = double + str(number%2)
         number//=2
    
    #for i in range(0,len(double)//2+1):
        # temp = 0
        # temp = double[i]
        # double[i] = double[-1 -i]
        # double[-1 -i] = temp
    
         
    double[-1] == double[0]
     
       
    print(double[-1])
    
ten_to_double(num)
