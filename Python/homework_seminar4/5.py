# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


poli1 = "81x^2 + 36x + 12 = 0".replace("x", " ").split()
poli2 = "2x^2 + 6x + 1 = 0".replace("x", " ").split()

def sum_poly(a, b):
    s_a = []
    s_b = []
    for i in a:
        if i.isnumeric():
            s_a.append(int(i))
    
    for e in b:
        if e.isnumeric():
            s_b.append(int(e))
    
    sum = []
    for n in range(0, len(s_a)):
        sum.append(s_a[n] + s_b[n])
    
    result = f'{sum[0]}x2 + {sum[1]}x + {sum[2]} = 0'
    return result

res = sum_poly(poli1, poli2)
print(res)
data = open('polynom_sum.txt', 'w')
data.write(res)
data.close()


#не получается открыть файлы o.TextIOWrapper name='poli_task5.txt' mode='r' encoding='cp1251'>
exit()
with open("poli_task5.txt", "w") as data:
    data.write("81x^2 + 36x + 12 = 0")

with open("poli2_task5.txt", "a") as data:
    data.write("2x^2 + 6x + 1 = 0")

data = open("poli_task5.txt", "r")
print(data)
