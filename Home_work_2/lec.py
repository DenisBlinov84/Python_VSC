# Задача 1
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# def get_count(number):
#     s = str(number)
#     if '.' in s:
#         return abs(s.find('.') - len(s)) - 1
#     else:
#         return 0


# a = input("Введите число --> ")
# x = int(get_count(a))
# y = float(a)
# if x != 0:
#     for i in range(x):
#         y *= 10
# y = int(y)
# b = 0
# for i in range(len(a) - 1):
#     b += y % 10
#     y //= 10
# print(b)


# print(s(53751))


# Задача 2
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('Введите число N -> '))


# def s(n):
#     i = 1
#     k = 1
#     for i in range(1, (n+1)):
#         k = k*i
#         print(k)


# s(n)


# Задача 3
# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input("Введите число n: "))


# def get_squerence(n):
#     s = 0
#     for i in range(1, n+1):
#         s += (1+1/i)**i
#     return(round(s, 2))


# print(get_squerence(n))


# Задача 4
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.

# import random

# n = int(input("Введите число n -> "))
# my_list = [random.randint(-n, n) for i in range(n)]

# print(my_list)

# prod = 1
# for i in range(len(my_list)):
#     prod *= my_list[my_list[i]]
# print(f"Результат равен = {prod}")


# Задача 5
# Реализуйте алгоритм перемешивания списка.

# import random
# lst = [random.randint(0,10) for i in range(random.randint(5,20))]
# print(f"исходный список:\n {lst}")
# random.shuffle(lst)
# print(f"список после перемешивания:\n{lst}")
