# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
k = int(input('введите степень К:'))

data = open('file.txt', 'w')

x = random.randint(0, 100)
print(x)
if k <= 2:
    result = ((2 * (x**k)) + (4 * k) + 5)
    print(result)
else:
    result = (2 * (x**3) + (4 * (x**(k-1)) + 5))

# data.writelines(f'Многочлен стпени {k} = {result}')  
data.writelines(f'{result}')
print(f'Многочлен степени {k} = ', result) 

# data.close()   

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
data.close()
exit()    