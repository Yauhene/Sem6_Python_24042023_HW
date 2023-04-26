﻿# Урок 6. Повторение списков

# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность 
# и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии:
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

print()

start_num = int(input('Ведите первый элемент прогрессии: '))
print()

difference = int(input('Ведите разность прогрессии: '))
print()

size_num = int(input('Ведите количество элементов прогрессии: '))
print()

progr_list = []

for i in range(1, size_num + 1):
    progr_list.append(start_num + (i-1) * difference)
    
print(progr_list)
print()

