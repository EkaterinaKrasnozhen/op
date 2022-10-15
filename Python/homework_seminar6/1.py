#3. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.

my_list = [3, 8, 3, 54, 5, 54]

# старый вариант решения
def unic_elem_2(i):
    uniq_list = []
    for i in my_list:
        if my_list.count(i) == 1:
            uniq_list.append(i)
    print(uniq_list)


unic_elem_2(my_list)

# новый вариант lambda
res  = list(filter(lambda x: my_list.count(x) == 1, my_list))
print(res)