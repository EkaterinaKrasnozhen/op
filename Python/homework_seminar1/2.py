# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = int(input('Введите число x '))
y = int(input('Введите число y '))
z = int(input('Введите число z '))


def true_or(l, k, m):
    a = not (l or k or m)
    b = not l and not k and not m
    res = a == b
    if (res == True):
        print('истинно')
    else:
        print('ложно')


true_or(x, y, z)
