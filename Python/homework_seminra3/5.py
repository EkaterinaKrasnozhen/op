# 5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def nega_fib(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    else:
        return nega_fib(n+2)-nega_fib(n+1)

list = []
for e in range (-8,0):
    list.append(nega_fib(e))
print(list)
print(nega_fib(-8))