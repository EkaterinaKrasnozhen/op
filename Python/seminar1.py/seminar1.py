#Задача 2: Найти максимальное из пяти чисел.
nums = [1,3,4,51,6]

def max_num(numbers):
    max = numbers[0]
    index = 0
    for e in numbers:
        if (numbers[index]>max):
             max = numbers[index]
        index+=1
    return max
print(max_num(nums))