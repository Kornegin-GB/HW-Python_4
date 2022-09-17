""" Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов. """
import random

# запись в файл


def write_file(path, string):
    with open(path, 'w') as data:
        data.write(string)

# создание коэффициентов многочлена


def create_mn(k):
    lst = [random.randint(0, 100) for i in range(k+1)]
    return lst

# создание многочлена в виде строки


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

# получение степени многочлена


def sq_mn(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num

# получение коэффицента члена многочлена


def k_mn(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num

# разбор многочлена и получение его коэффициентов


def calc_mn(string):
    string = string[0].replace(' ', '').split('=')
    string = string[0].split('+')
    lst = []
    len_string = len(string)
    if sq_mn(string[-1]) == -1:
        lst.append(int(string[-1]))
        len_string -= 1
    degree = 1  # степень
    index = len_string-1  # индекс
    while index >= 0:
        if sq_mn(string[index]) != -1 and sq_mn(string[index]) == degree:
            lst.append(k_mn(string[index]))
            index -= 1
            degree += 1
        else:
            lst.append(0)
            degree += 1

    return lst


# создание двух файлов
k1 = int(input("Введите натуральную степень для первого файла k = "))
k2 = int(input("Введите натуральную степень для второго файла k = "))
koef1 = create_mn(k1)
koef2 = create_mn(k2)
write_file("file1.txt", create_str(koef1))
write_file("file2.txt", create_str(koef2))

# нахождение суммы многочлена

with open('file1.txt', 'r') as data:
    st1 = data.readlines()
with open('file2.txt', 'r') as data:
    st2 = data.readlines()
print(f"Первый многочлен {st1}")
print(f"Второй многочлен {st2}")
lst1 = calc_mn(st1)
lst2 = calc_mn(st2)
len_list_1 = len(lst1)
if len(lst1) > len(lst2):
    len_list_1 = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(len_list_1)]
if len(lst1) > len(lst2):
    len_list_2 = len(lst1)
    for i in range(len_list_1, len_list_2):
        lst_new.append(lst1[i])
else:
    len_list_2 = len(lst2)
    for i in range(len_list_1, len_list_2):
        lst_new.append(lst2[i])
write_file("file3.txt", create_str(lst_new))
with open('file3.txt', 'r') as data:
    st3 = data.readlines()
print(f"Результирующий многочлен {st3}")
