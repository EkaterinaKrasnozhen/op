#6. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#Входные и выходные данные хранятся в отдельных текстовых файлах.




strng1 = 'WWabWWaCCa'
count = 1
char = strng1[0]
res = ''
for e in range(1,len(strng1)):
    if strng1[e] == char:
        count+=1
    else:
        res = res+str(count)+char
        char = strng1[e]
        count = 1
    if e == len(strng1)-1:
     res = res+str(count)+char
        

print(res)


 
 

