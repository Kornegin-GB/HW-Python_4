""" Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
Пример:
k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0 """

import random

k = int(input("K = "))
polynomial = ''
while k >= 0:
    rand = random.randint(0, 100)
    if k == 0:
        polynomial = polynomial + f"{rand} = 0"
    elif k == 1:
        polynomial = polynomial + f"{rand}x + "
    else:
        polynomial = polynomial + f"{rand}x^{k} + "

    k -= 1

with open("file.txt", 'w') as text:
    text.write(polynomial)
