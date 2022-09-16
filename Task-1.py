""" Вычислить число c заданной точностью d
Пример:
при $d = 0.001, π = 3.141.$ $10^{-1} ≤ d ≤10^{-10}$ """

import math

d = float(input("Введите точность расчета: "))
d_len = len(str(d).split('.')[1])
print(round(math.pi, d_len))
