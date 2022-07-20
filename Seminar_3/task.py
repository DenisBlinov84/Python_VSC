# Задача 1
# Задайте список. Напишите программу, которая определит, присутствует ли
# в заданном списке строк некое число
# '12' -> ['asd12', '12', 'asd', '87'] -> 'asd12', '12'

# my_list = ['asd12', '12', 'asd', '87']
# for i in my_list:
#     if '12' in i:
#         print(i)

# def there_is_number(list, number):
#     result = False
#     for elements in list:
#         if len(elements) == len(number):
#             if elements == number:
#                 result = True
#                 print(elements)

#         if len(elements) > len(number):
#             for i in range(len(elements) - len(number) + 1):
#                 if elements[i: i + len(number)] == number:
#                     result = True
#                     print(elements)
#     return result


# list = ['trvwe12', '123']
# number = '12'
# if there_is_number(list, number):
#     print(f'Число {number} есть.')
# else:
#     print(f'Числа {number} нет.')

# Задача 2
# Напишите программу, которая определит позицию второго
# вхождения строки в списке , либо сообщит, что её нет


# count = 0
# my_list = ["йцу", "фав", "ячс", "цук", "йцукен", "йцу", "йцу", "йцу"]
# for i in range(len(my_list)):
#     if my_list[i] == 'йцу':
#         count += 1

#         if count > 1:
#             print(i)
#             break


# Задача 3
# Реализуйте алгоритм задания случайных чисел без использования
# встроеного генератора псевдослучайных чисел

# import time

# a = str(time.time())
# b = a[-1] + a[-2]
# print(int(b))

# import time
# i = int(input('Введите длинну числа: '))
# ms = int(((time.time() % 1) * (10 ** (i + 1))) % (10 ** (i)))
# print(ms)
