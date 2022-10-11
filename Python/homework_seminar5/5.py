# 5. Создайте программу для игры в "Крестики-нолики".


list1 = [
    ["  1", "   2  ", " 3  "],
    ["a", "|__|", "|__|", "|__|"],
    ["b", "|__|", "|__|", "|__|"],
    ["c", "|__|", "|__|", "|__|"],
]
# def cross_field(lis):
#  for i in range(0,len(lis)):
#   for e in lis[i]:
#         print(f'{e}',end='')
#   print()

# cross_field(list1)

move_x = (input("Введите координаты вашего хода: ").replace(" ", "").replace(",", "").replace(".", ""))
move_y = (input("Введите координаты вашего хода: ").replace(" ", "").replace(",", "").replace(".", ""))

list1 = [["  1", "   2  ", " 3  "],
    ["a", "|__|", "|__|", "|__|"],
    ["b", "|__|", "|__|", "|__|"],
    ["c", "|__|", "|__|", "|__|"]]

# list1[1][1] = '| x|'

dictionary = \
{
    "1a": "11",
    "2a": "12",
    "3a": "13",
    "1b": "21",
    "2b": "22",
    "3b": "23",
    "1c": "31",
    "2c": "32",
    "3c": "33",
}

a = dictionary[move_x]
b = dictionary[move_y]


def cross_field(lis, x, y):
    dictionary = \
{
    "1a": "11",
    "2a": "12",
    "3a": "13",
    "1b": "21",
    "2b": "22",
    "3b": "23",
    "1c": "31",
    "2c": "32",
    "3c": "33",
}
    count = 0
    for i in range(0, len(lis)):
        for e in lis[i]:
            
              print(f"{e}", end="")
              lis[int(x[0])][int(x[1])] = "| x|"
              count += 1
            
            # else:
            #     print(f"{e}", end="")
            #     lis[int(y[0])][int(y[1])] = "| 0|"
            #     count += 1
                
        print()
        
    move = (input("Введите координаты вашего хода: ").replace(" ", "").replace(",", "").replace(".", ""))  
    x = dictionary[move]
    print(x)


cross_field(list1, a, b)
