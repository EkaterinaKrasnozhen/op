# 1. Вычислить число c заданной точностью d
# 	Пример:	
# 	при d = 0.001, π = 3.141        10-1 <= d <= 10-10

import math

d = input('Введите значение d в пределах 10-1 <= d <= 10-10:  ')

def d_pi(d1):
    count = 0
    pi = math.pi
    for i in d1:
        if i!=',' and i!='.':
            count+=1
    print(round(pi,count-1))
    
d_pi(d)