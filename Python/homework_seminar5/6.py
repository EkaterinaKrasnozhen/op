# 6. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# with open("hw_sem5_6py.txt", "a") as data:
#      data.write("WWabWWaCCa")

data = open("hw_sem5_6py.txt", "r")
string1 = data.read()
print(string1)
data.close()
print()
#string1 = "WWabWWaCCa"


def rle(strng1):
    count = 1
    char = strng1[0]
    res = ""
    for e in range(1, len(strng1)):
        if strng1[e] == char:
            count += 1
        else:
            res = res + str(count) + char
            char = strng1[e]
            count = 1
        if e == len(strng1) - 1:
            res = res + str(count) + char

    return res

file = rle(string1)
print(f' результат сжатия RLE: {rle(string1)}')


def un_rle(res):
    str1 = ""
    for i in range(0, len(res), 2):
        str1 = str1 + (res[i + 1] * int(res[i]))
    return str1

print(f' результат восст-ния:  {un_rle(file)}')