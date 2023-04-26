# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

print()
num_list = []
out_num_list = []
print('Введите последовательность целых чисел, разделяя их запятой либо пробелом: ', end = '\n')
num_range = input()
#--- обработка принятой строки, формирование списка значений из нее
num_range = num_range.replace(',', ' ')
num_range = num_range.split()
num_list = list(num_range)
print()
#--- ввод границ диапазона, заполнение списка
min_limit = int(input('Введите нижнюю границу диапазона(минимальное число): '))
print()
max_limit = int(input('Введите верхнюю границу диапазона(максимальное число): '))
print()

for i in range(0, len(num_list)):
    num_list[i] = int(num_list[i])
    if min_limit <= num_list[i] <= max_limit:
        out_num_list.append(num_list[i])
#--- сортировка списка чисел в границах диапазона
min_num = out_num_list[0]
for i in range(0,len(out_num_list)):
    min_num = out_num_list[i]
    for j in range(i+1,len(out_num_list)):

        if  out_num_list[j] < min_num:
            temp = out_num_list[i]
            out_num_list[i] = out_num_list[j]
            out_num_list[j] = temp
            min_num = out_num_list[i]

print('Исходный список: ', num_list)
print(f'Числа, входящие в диапазон значений от {min_limit} до {max_limit}: {out_num_list}')
print()