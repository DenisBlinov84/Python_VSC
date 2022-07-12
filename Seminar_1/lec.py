# Задача 1
# Принимает на вход два числа и проверяет, является ли одно число квадратом другого
# 5, 25 -> да

# a = int(input('Введите число a = '))
# b = int(input('Введите число b = '))

# if b == a * a:
#     print(f'{a}, {b} -> yes')
# elif a == b * b:
#      print(f'{a}, {b} -> yes')
# else:
#       print(f'{a}, {b} -> no')

# if((b == a * a) or (a == b * b)):
#     print(f'{a}, {b} -> yes')
# else:
#     print(f'{a}, {b} -> no')

# print('yes' if ((a == b*b) or (b == a*a)) else 'no')


# Задача 2
# На вход принимает 5 чисел и находит максимальное из них
# -1, 4, 8, 7, 5 -> 8

# maxx = 0
# for i in range(5):
#     x = int(input('--> '))
#     if i == 0:
#         maxx = x
#     elif x > maxx:
#         maxx = x
# print(maxx)

# my_list = [5, 2, 9, 1, 3]
# i = 1
# maxx = my_list[0]
# while i < len(my_list):
#     if my_list[i] > maxx:
#         maxx = my_list[i]
#     i += 1
# print(maxx)


# Задача 3
# Будет на вход принимать число N и выводить числа от -N до N
# -5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# n = int(input('Введите число N -> '))
# for i in range(-n, (n+1)):
#     print(i, end=' ')

# n = int(input('Введите число N -> '))
# a = -n
# while a < n + 1:
#     print(a, end=' ')
#     a += 1


# Задача 4
# Будет на вход принимать дробь и показывать первую цифру дробной части числа
# 6.78 -> 7
# 5 -> нет

# x = float(input('-> '))
# x *= 10
# x = int(x)
# x= x % 10
# if(x == 0):
#     print('no')
# else:
#     print(x)

# a = '6,78'
# for i in range(len(a)):
#     if a[i] == ',':
#         print(a[i + 1])


# Задача 5
# Принимает на вход число и проверяет,
# кратно ли оно (5 и 10) или (15, но не 30)

# x = int(input('--> '))
# if((x % 5 == 0 and x % 10 == 0) or (x % 15 == 0 and x % 30 != 0)):
#     print('yes')
# else:
#     print('no')