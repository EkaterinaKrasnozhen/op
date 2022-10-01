text = ['красный', '56', 'нет', 'игра', 'слава']


def mash_list(my_list):
    len_half = (len(my_list)-1)//2
    print(len_half)
    for i in range(0, len_half):
        temp = my_list[len(my_list)-1-i]
        my_list[len(my_list)-1-i] = my_list[i]
        my_list[i] = temp
    print(my_list)

mash_list(text)