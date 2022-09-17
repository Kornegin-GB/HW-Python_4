""" Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
Пример:
k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0 """

import random

# запись в файл


def write_file(path, string):
    with open(path, 'w') as data:
        data.write(string)


def create_mn(k):
    lst = [random.randint(0, 100) for i in range(k+1)]
    return lst


def create_str(lst_kof):
    lst = lst_kof[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr


k = int(input("Введите натуральную степень для первого файла k = "))
koef1 = create_mn(k)
write_file("file.txt", create_str(koef1))

with open('file.txt', 'r') as data:
    print(data.readlines())
