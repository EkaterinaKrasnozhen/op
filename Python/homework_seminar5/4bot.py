
import random


choice = int(input(" Ход игрока 1. Сколько конфет вы забираете? "))
candy = 10

def candy_mines(number, user_choice):  # number = количество конфет, user_choice - цифра ск выбрал пользователь
    count = 0
    user = 0
    max_value = 2
    while number > 0:
        if user_choice in range(1, 3):
            number -= user_choice
            if number == 0:
                print(f"Игра окончена, победил игрок {user}")
                break
            print(number)
            count += 1
            
            if not count % 2:
                user_choice = int(input("Игрок 1, ск еще? "))
                user = 1
            
            else:
                if user_choice%2==0:
                    user_choice = random.randint(1,max_value)
                    if user_choice>number:
                        user_choice = random.randint(1,number)
                #user_choice = random.randint(1,2)
                user_choice = number%(max_value+1)
                print(f'Ход компьютера = {user_choice} ')
                user = 'компьютер'
            
            if number < user_choice:
                print("остаток меньше введенного числа")
                user_choice = int(input("ск еще? "))

        else:
            print("неверное число")
            user_choice = int(input("ск еще? "))


candy_mines(candy, choice)