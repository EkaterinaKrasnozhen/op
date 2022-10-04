#2. Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

find = input('Введите искомое число: ')
my_list = ['шла', 'Саша', '5', '25', '12']
def find_num_in_list(user_input, list1):
    if user_input in list1:
        return True
    else: return False
    
print(find_num_in_list(find, my_list))