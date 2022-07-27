# Задача 1
# Вычислить число pi c заданной точностью d
# Пример: 
# при d = 0.001,  pi = 3.141. 10^(-1) <= d10 <= 10^(-10)

# import math
# from math import pi

# n = pi
# print(n)
# print(round(n, 3))

# Формула Бэйли — Боруэйна — Плаффа

# n = 100
# my_pi = sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) for x in range(n))

# print(my_pi)

# Ряд Лейбница

# n = 20000000

# mypi = 4 * (sum(1/x for x in range(1, n + 1, 4)) +
#             sum(-1/x for x in range(3, n + 1, 4)))

# print(format(mypi, '.100'))


# Задача 2
# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

# import math

# def is_prime(n):
#     primes = [2]
#     for num in range(3, n + 1, 2):
#         if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
#             primes.append(num)
#     return primes

# def get_prime_factors(n, primes):
#     fact = []
#     for i in primes:
#         while n % i == 0:
#             n = n / i
#             fact.append(i)
#     return fact

# n = int(input('Введите число: '))

# primes = is_prime(n)
# factors = get_prime_factors(n, primes)
# print(factors)

# def testing(n, factors):
#     return math.prod(factors) == n       

# print(testing(n, factors))

# def task31 (n):
#     i = 2
#     array = []
#     while n != 1: 
#         if n % i == 0:
#             array.append(i) #3
#             n = n / i
#             i = 2
#         else: 
#             i += 1
#     return (array)

# print (task31 (5))



# Задача 3
# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

# from random import randint

# def create_list(size, m, n):
#     return [randint(m, n) for i in range(size)]

# def get_unic_value(list):
#     return [i for i in set(list)]

# size = 10
# m = 1
# n = 10

# origin = create_list(size, m, n)
# print(origin)
# print(get_unic_value(origin))



# Задача 4
# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
#  k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# from random import randint
# import itertools

# k = randint(2, 7)

# def get_ratios(k):
#     ratios = [randint(0, 10) for i in range (k + 1)]
#     while ratios[0] == 0:
#         ratios[0] = randint(1, 10) 
#     return ratios

# def get_polynomial(k, ratios):
#     var = ['*x^']*(k-1) + ['*x']
#     polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
#     for x in polynomial:
#         x.append(' + ')
#     polynomial = list(itertools.chain(*polynomial))
#     polynomial[-1] = ' = 0'
#     return "".join(map(str, polynomial)).replace(' 1*x',' x')


# ratios = get_ratios(k)
# polynom1 = get_polynomial(k, ratios)
# print(polynom1)

# with open('33_Polynomial.txt', 'w') as data:
#     data.write(polynom1)


# # Второй многочлен для следующей задачи:

# k = randint(2, 5)

# ratios = get_ratios(k) 
# polynom2 = get_polynomial(k, ratios)
# print(polynom2)

# with open('33_Polynomial2.txt', 'w') as data:
#     data.write(polynom2)



# Задача 5
# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# import re
# import itertools


# file1 = r'Home_work_4/33_Polynomial.txt'
# file2 = r'Home_work_4/33_Polynomial2.txt'
# file_sum = r'Home_work_4/Sum_polynomials.txt'

# # Получение данных из файла

# def read_pol(file):
#     with open(str(file), 'r') as data:
#         pol = data.read()
#     return pol

# # Получение списка кортежей каждого (<коэффициент>, <степень>)

# def convert_pol(pol):
#     pol = pol.replace('= 0', '')
#     pol = re.sub("[*|^| ]", " ", pol).split('+')
#     pol = [char.split(' ') for char in pol]
#     pol = [[x for x in list if x] for list in pol]
#     for i in pol:
#         if i[0] == 'x': i.insert(0, 1)
#         if i[-1] == 'x': i.append(1)
#         if len(i) == 1: i.append(0)
#     pol = [tuple(int(x) for x in j if x != 'x') for j in pol]
#     return pol

# # Получение списка кортежей суммы (<коэф1 + коэф2>, <степень>)

# def fold_pols(pol1, pol2):   
#     x = [0] * (max(pol1[0][1], pol2[0][1] + 1))
#     for i in pol1 + pol2:        
#         x[i[1]] += i[0]
#     res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
#     res.sort(key = lambda r: r[1], reverse = True)
#     return res

# # Составление итогового многочлена

# def get_sum_pol(pol):
#     var = ['*x^'] * len(pol)
#     coefs = [x[0] for x in pol]
#     degrees = [x[1] for x in pol]
#     new_pol = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
#     for x in new_pol:
#         if x[0] == '0': del (x[0])
#         if x[-1] == '0': del (x[-1], x[-1])
#         if len(x) > 1 and x[0] == '1' and x[1] == '*x^': del (x[0], x[0][0])
#         if len(x) > 1 and x[-1] == '1': 
#             del x[-1]
#             x[-1] = '*x'
#         x.append(' + ')
#     new_pol = list(itertools.chain(*new_pol))
#     new_pol[-1] = ' = 0'
#     return "".join(map(str, new_pol))

# def write_to_file(file, pol):
#     with open(file, 'w') as data:
#         data.write(pol)

# pol1 = read_pol(file1)
# pol2 = read_pol(file2)
# pol_1 = convert_pol(pol1)
# pol_2 = convert_pol(pol2)

# pol_sum = get_sum_pol(fold_pols(pol_1, pol_2))
# write_to_file(file_sum, pol_sum)

# print(pol1)
# print(pol2)
# print(pol_sum)
