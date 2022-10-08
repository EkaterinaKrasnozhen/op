# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# 	Пример:
# 	k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from lib2to3.pygram import Symbols
import random



input_x = symbol('x')
print(input_x)
degree_num = 4

def polynom(k,x):
    lis = []
    num = random.randint(0,100)
    print(num)
    for i in range(1,k+1):
        
        lis.append(i)
    print(lis)
    
    
        
    
print(polynom(degree_num, input_x))