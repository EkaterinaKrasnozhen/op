# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.



def true_or(l, k, m):
    a = not (l or k or m)
    b = not l and not k and not m
    res = a == b
    if (res == True):
        print('истинно')
    else:
        print('ложно')
for x in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                print(f' x {x} y {y} z {z}')
                (true_or(x, y, z))




