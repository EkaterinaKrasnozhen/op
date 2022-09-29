# 4. Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в списке positions - создайте этот список (например: positions = [1, 3, 6]).

number = int(input('Введите число N '))
positions = [1,3,6]
def multi_position_list(n):
    if n < 0:
        n=n*-1
    result = []
    for i in range(-n, n+1):
            result.append(i)
    return result
numbers = multi_position_list(number)
for i in positions:
   # print (numbers[i], end='', )
    print ('{} '.format(numbers[i]), end='')
