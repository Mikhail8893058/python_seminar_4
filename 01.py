# Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141
import math
from unittest import result
n = int(input('Введите число с заданной точность:'))
a = math.pi
result = '{:.' + str(n) + 'f}'
print(result.format(a))