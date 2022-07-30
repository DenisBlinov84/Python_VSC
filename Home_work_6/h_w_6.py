# Задача 1
# Задать список из чисел строкового типа. Преобразовать в список из целых чисел.

# old_list = ['1', '2', '3', '4', '5', '6', '7']
 
# new_list = []
# for item in old_list:
#     new_list.append(int(item))
 
# print (new_list)

# old_list = ['1', '2', '3', '4', '5', '6', '7']
# new_list = list(map(int, old_list))
# print (new_list)



# Задача 2
# Создать список со значением скорости в милях.
# Перевести в список скоростей в киломеирах.

# mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
# kilometer_distances = list(map(lambda x: x * 1.6, mile_distances))
 
# print (kilometer_distances)



# Задача 3
# Задать два списка. Посчитать суммы элементов этих списков с одинаковыми индексами.
# Результат вывести в ввиде списка.

# l1 = [1,2,3]
# l2 = [4,5,6]
 
# new_list = list(map(lambda x,y: x + y, l1, l2))
# print (new_list)
 


#  Задача 4
# Задать список. Вычислить сумму элементов списка.

# from functools import reduce
# items = [1,2,3,4,5]
# sum_all = reduce(lambda x,y: x + y, items)
 
# print (sum_all)



# Задача 5
# Задать список. Вычислить наибольший элемент в списке.

# from functools import reduce
# items = [1, 24, 17, 14, 9, 32, 2]
# all_max = reduce(lambda a,b: a if (a > b) else b, items)
 
# print (all_max)



# Задача 6
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите сумму элементов на указанных позициях.

# import random
# n = int(input("Введите число n -> "))
# my_list = [random.randint(-n, n) for i in range(n)]

# from functools import reduce
# sum_all = reduce(lambda x,y: x + y, my_list)
# print (sum_all)

# Задача 7
# Реализуйте алгоритм перемешивания списка.

# import random
# lst = [random.randint(0,10) for i in range(random.randint(5,20))]
# print(f"исходный список:\n {lst}")
# random.shuffle(lst)
# print(f"список после перемешивания:\n{lst}")