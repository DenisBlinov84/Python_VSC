# Задача 1
# Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка, стоящих на нечётной позиции.
# Пример:
#  [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# range(1, len(lst),2) # Чтобы сразу получить нечётные индексы

# my_list = [2, 3, 5, 9, 3]
# s = 0
# for i in range(len(my_list)):
#     if i % 2 != 0:
#         s += my_list[i]
# print(s)

# def sum_odd_index(lst):
#     s = 0
#     for i in range(len(lst)):
#         if i % 2 != 0:
#             s += lst[i]
#     print(f"Сумма равна: {s}")

# lst = [2, 3, 5, 9, 3]
# sum_odd_index(lst)


# Задача 2
# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
#	[2, 3, 4, 5, 6] => [12, 15, 16];
#	[2, 3, 5, 6] => [12, 15]

# lst = [2, 3, 4, 5, 6]
# if len(lst) % 2 != 0:
#     l = len(lst)//2 + 1
# else:
#     l = len(lst)//2

# my_list = []
# for i in range(l):
#     x = lst[i]*lst[len(lst)-i-1]
#     my_list.append(x)
# print(my_list)


# def mult_lst(lst):
#     l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
#     new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
#     print(new_lst)

# lst = [2, 3, 4, 5, 6]
# mult_lst(lst)


# Задача 3
# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# lst = [1.1, 1.2, 3.1, 5, 10.01]
# min = 1
# max = 0
# x = 0
# for i in range(len(lst)):
#     x = float((int(lst[i]*100)) % 100)/100
#     if x != 0:
#         if max < x:
#             max = x
#         if min > x:
#             min = x
# print(f'-> {max-min}')



# Задача 4
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# s = ""
# n = int(input("Введите число -> "))
# while n != 0:
#     s = str(n%2) + s
#     n //=2
# print(s)



# Задача 5
# Задайте число. Составьте список чисел Фибоначчи, в том числе
# для отрицательных индексов. 
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи]

# n = int(input('Введите число: '))
# n+=1
# def get_fibonacci(n):
#     fibo_nums = []
#     a, b = 1, 1
#     for i in range(n-1):
#         fibo_nums.append(a)
#         a, b = b, a + b
#     a, b = 0, 1
#     for i in range (n):
#         fibo_nums.insert(0, a)
#         a, b = b, a - b
#     return fibo_nums

# fibo_nums = get_fibonacci(n)
# print(get_fibonacci(n))
# print(fibo_nums.index(0))


