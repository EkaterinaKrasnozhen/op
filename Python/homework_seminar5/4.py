# 4. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

print("Всего 2021 конфета, за один ход можно взять от 1 до 28, выиграет тот, кто заберет последние конфеты")
candy = 100
choice = int(input("Сколько конфет вы забираете? "))


def inp(n):
    max_value = 28
    num = range(1, max_value + 1)
    if n not in num:
        return False
    else:
        return True


inp(choice)

# while candy>0:
# if inp(choice):
# remains = lambda x,y: x-y


def candy_mines(number, user_choice):  # number = количество конфет, user_chice - цифра ск выбрал пользователь
    while number > 0:
        if inp(user_choice):  # если введено верное число вычитаем
            number -= user_choice
            print(number)
            user_choice = int(input("ск еще? "))    # if candy > 0:
        else:
            print('неверное число') 
    return number

#res = candy_mines(candy, choice)


print(candy_mines(candy, choice))
