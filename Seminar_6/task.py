# Перемножить элементы списков:
# def dlb(lst: list) -> list:
#     count_dbl = (len(lst) + 1) // 2
#     res_list = [lst[i]*lst[-i-1] for i in range(count_dbl)]
#     return res_list


# list_1 = [[2, 3, 4, 5], [2, 3, 4, 5, 6, ]]
# print(list(map(dlb, list_1)))

# Распоковать элементы:
# def f(a_1, a_2, a_3):
#     print(a_1, a_2, a_3)

# tpl = (1, 2, 3)
# f(*tpl)


# Задача 1
# Дана последовательность чисел. Получить список уникальных элементов
# заданной последовательности.
# Пример:
# [1,2,3,5,1,5,3,10] => [2,10]

# Вариант 1:
# my_list = [1, 2, 3, 5, 1, 5, 3, 10]
# res = []
# for item in my_list:
#     if my_list.count(item) == 1:
#         res.append(item)
# print(res)

# Вариант 2:
# my_list = [1, 2, 3, 5, 1, 5, 3, 10]
# res = [item for item in my_list if(my_list.count(item) == 1)]
# print(res)

# Вариант 3:
# my_list = [1, 2, 3, 5, 1, 5, 3, 10]
# def f(item): return my_list.count(item) == 1


# res = list(filter(f, my_list))
# print(res)

