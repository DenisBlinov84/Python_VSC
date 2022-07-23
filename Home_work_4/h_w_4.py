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

# with open('Polynomial.txt', 'w') as data:
#     data.write(polynom1)






