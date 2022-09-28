# 3.Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.
a_str = input('Введите строку а : ')
b_str = input('Введите строку b : ')

def coincid(a,b):
    count=0
    for i in a:
        for e in b:
            if i==e:
                count+=1
    return count

print(coincid(a_str,b_str))

#print(a_str.count(b_str))
