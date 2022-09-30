# 5. Реализовать алгоритм перемешивания списка.

text = ['красный', '56', 'нет', 'игра']


def mash_list(my_list):
    
    for i in range(0, len(my_list)-1):
        temp = my_list[len(my_list)-1-i]
        my_list[len(my_list)-1-i] = my_list[i]
        my_list[i] = temp
# не пойму, почему дальше не идет перемешивание, а только крайние элементы?
    print(my_list)


mash_list(text)
