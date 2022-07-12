# Принимает на вход число N и выдаёт
# последовательность из N членов
# Для N = 5: 1, -3, 9, -27, 81

# def searchNumber(a: int, b: int) -> list :
#     my_list = [1]
#     while len(my_list) < a:
#         my_list.append(my_list[-1] * b)
#     return my_list


# print(searchNumber(5, -3))

# def print_numbers(x):
#     vivod = 1
#     for i in range(x):
#         print(vivod, end=' ')
#         vivod = vivod * -3


# n = int(input('-->'))
# print_numbers(n)


# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другую.

# st1 = 'привет, мир, т, привет!'
# st2 = ','


# def str(st1, st2):
#     t = 0
#     for i in range(len(st1) - len(st2)):
#         if (st1[i: i + len(st2)] == st2):
#             t += 1
#     return t


# print(str(st1, st2))


# st1 = "1234567890"
# print(st1[1:4]) # срез с 1 по 4 элемент
# print(st1[1:4:2]) # с шагом 2



# symbol = "so"
# base_string = "some personal symbols"
# position = 0
# qty = 0
# while(True):
#     position = base_string.find(symbol, position)
#     if position == -1:
#         break
#     else:
#         position += 1
#         qty += 1
# print(qty)