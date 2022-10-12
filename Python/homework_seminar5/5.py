
list1 = [["  1", "   2  ", " 3", "\n"],
         ["a", "|__|", "|__|", "|__|", "\n"],
         ["b", "|__|", "|__|", "|__|", "\n"],
         ["c", "|__|", "|__|", "|__|", "\n"]]

print('введите координаты хода:')
for i in range(0, len(list1)):
    for e in list1[i]:
        print(f"{e}", end="")

def cross_field(lis):
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
    count = 1
    x_steps = set()
    y_steps = set()
    while count < 10: 
        if count % 2:
            x = dictionary[input(' ходят X: ')]
            for i in range(0, len(lis)):
                for e in lis[i]:
                    print(f"{e}", end= "")
                    lis[int(x[0])][int(x[1])] = "| x|"
                    x_steps.add(x)          

        else:
            x = dictionary[input(' ходят 0: ')]
            for i in range(0, len(lis)):
                for e in lis[i]:
                    print(f"{e}", end= "")
                    lis[int(x[0])][int(x[1])] = "| 0|"
                    y_steps.add(x)
                    
        count += 1
        
        print(f'{x_steps = }')
        print(f'{y_steps = }')
        win = ({'11', '12', '13'},
               {'21', '22', '23'},
               {'31', '32', '33'},
               {'11', '21', '31'},
               {'12', '22', '32'},
               {'13', '23', '33'},
               {'11', '22', '33'},
               {'13', '22', '31'})
        for i in win:
            if x_steps >= i:
                return 'выиграли Х'
                
            elif y_steps >= i:
                return 'выиграли 0'
                
            


print(cross_field(list1))