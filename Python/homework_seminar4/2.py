# 2. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

num = int(input("Введите натуральное число: "))


def nat_divider(n):
    div_2 = 2
    lis = []
    while div_2 * div_2 <= n:

        while n % div_2 == 0:
            n //= div_2  # вот до этого момента сама додумалась
            lis.append(div_2)
        div_2 += 1  # это подсмотрела
    if n > 1:
        lis.append(n)
    return lis


print(*nat_divider(num))


# n = 80
# sieve = set(range(2,n+1))
# prime_list = []
# while sieve:
#     prime = min(sieve)
#     prime_list.append(prime)
#     sieve -= set(range(prime,n+1,prime))

# print(sieve)