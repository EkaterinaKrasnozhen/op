# 3. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.

my_list = [3, 3, 8, 3, 54, 5, 3, 54]


def unic_elem(a):
    index = 0
    b = []
    c = a
    while index < len(c)-1:
        for i in range(1, len(a)-1):

            if c[index] == a[i]:
                print(f" с[{index}] = {c[index]}, a[{i}] = {a[i]}")
                b.append(index)
                b.append(i)

                print(f" index {index}")
                i+=1
            else:
                index += 1
            
        
    list_index = set(b)

    print(list_index)


unic_elem(my_list)
# почему не сравниваются дальше индексы?