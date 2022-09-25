# Задача 7 Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                print(f' x {x} y {y} z {z}')
                print(logical(x, y, z))
