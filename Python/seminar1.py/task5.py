# задача 5 Дано число. Проверить кратно ли оно 5 и 10 или 15, но не 30.
num = int(input('Введите целое число '))
def multi_nums(number):
    if(number%30 ==0):
        print(f'число {number} не отвечает условиям')
    elif (number%5 == 0) | (number%10 == 0) | (number%15 == 0):
        print(f'число {number} кратно 5, 10 или 15')
    
    else:
        print(f' число {number} не крато 5, 10 или 15 или 30')
multi_nums(num)