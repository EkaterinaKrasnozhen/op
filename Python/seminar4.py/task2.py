# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения;
# 2) с помощью дополнительных библиотек Python.

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

list1 = [a, b, c]


def discrim(nums):
    a1, b1, c1 = nums
    d = b**2 - 4 * a * c
    if d == 0:
        x1 = -b / 2 * a
        return x1, None
    elif d > 0:
        x1 = round((-b + d**0.5) / 2 * a, 2)
        x2 = round((-b - d**0.5) / 2 * a, 2)
        return x1, x2
    else:
        return None, None


print(discrim(list1))
