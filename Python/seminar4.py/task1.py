my_string = input("введите числа через пробел ").split(" ")


def str_to_num(str):

    max_n = str[0]
    min_n = str[0]

    for i in range(0, len(str)):
        if int(max_n) < int(str[i]):
            max_n = str[i]
        elif int(min_n) > int(str[i]):
            min_n = str[i]

    print(max_n, min_n)


str_to_num(my_string)
