# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# 	Пример:
# 	k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random

degree_num = 2


def polynom(k):
    x = []
 
    for i in range(0, k - 1):
        x.append(f"{random.randint(0,100)}x^{k-i} + ")
    x.append(f"{random.randint(0,100)}x + ")
    x.append(f"{random.randint(0,100)} = 0")
    a = "".join(str(n) for n in x)

    return(a)

result = polynom(degree_num)
print(result)
data = open('polynom.txt', 'w')
data.write(result)
data.close()