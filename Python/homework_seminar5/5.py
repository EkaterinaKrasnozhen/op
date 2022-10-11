#5. Создайте программу для игры в "Крестики-нолики".




# list1 = [['  1', '   2  ', ' 3  '],['a','|__|','|__|','|__|'],['b','|__|','|__|','|__|'],['c','|__|','|__|','|__|']]
# def cross_field(lis):
#  for i in range(0,len(lis)):
#   for e in lis[i]:
#         print(f'{e}',end='')
#   print()

# cross_field(list1)

move = input('Введите координаты вашего хода: ').replace(' ','').replace(',','').replace('.','')
print(move[1])
                                                  

