# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]
def natural_number(n):
    number_list = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            number_list.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        number_list.append(n)
    return number_list

num = natural_number(29)
print(num)