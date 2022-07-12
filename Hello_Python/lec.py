# # print('hello word')

# a = 123
# b = 1.23

# # print(type(a))
# # print(a)
# # print(type(b))
# # print(b)

# # value=None
# # print(type(value))
# # value=1234
# # print(type(value))
# # print(value)

# s = 'hello \nword'  # \n -перенос на другую строку
# # можно использовать " чтобы они отразилсиь в выводе строки, или поменять местами "'"
# s = 'hello "word'
# print(s)  # вывод строки

# print(a, '-', b, '-', s)
# print('{1}-{2}-{0}'.format(a, b, s))
# print(f'{a}-{b}-{s}')

# f = True  # или False
# print(f)

# можно использовать разные типы данных, но в одном списке не стоит
# list = ['1', '2', '3', 1, 2, 3, 1.23, False]
# print(list)

# print('Введите a')
# a = input()
# print('Введите b')
# b = input()
# print(a, b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')]

# print('Введите a')
# a = int(input())
# print('Введите b')
# b = int(input())
# print(a, '+', b, '=', a+b)

# a = 2
# b = 7
# c = 2**7  # возведение в степень
# print(c)

# a = 1.365688477
# b = 3
# c = round(a*b, 5)  # округление до 5 знаков
# print(c)

# a = 5
# a += 3 # a = a + 3
# print(a)

# a = 1 < 4 and 5 > 3
# print(a)

# a = 1 == 3 # сравнение
# print(a)

# a = 1 != 3 # неравенство
# print(a)

# a = 'qwe'
# b = 'qwe'
# print(a == b)

# a = [1, 2] # сравниваем списки
# b = [1, 2]
# print(a == b)

# func = 1
# T = 4
# x = 2
# print(func < T > x)

# f = 1 < 4 or 4 > 5  # или - верно когда хотя бы одно из высказываний верно
# print(f)

# f = [1, 2, 3, 4]
# print(f)
# print(not 2 in f)

# is_odd = f[0] % 2 == 1
# print(is_odd)

# is_odd1 = not f[0] % 2 # 0-False 1-True
# print(is_odd1)

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)

# for i in 1,2,3,4,5:
#     print(i**2)

# list =  [1,2,3,4,5] # список
# for i in list:
#     print(i**2)

# r = range(10) # объект
# for i in r:
#     print(i)

# for i in range (1 , 10, 2): # от 1 до 10 и приращение 2
#     print(i)

# for i in 'qwe-rty':
#     print(i)

# help(str) # если забыли что делает функция

# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # с
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # съешь ещё этих мягких французских булок
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2]
# print(text)

# numbers = [1,2,3,4,5]
# print(numbers)
# ran = range(1,6)
# print(type(ran))
# numbers = list(ran)
# print(type(numbers))

# print(numbers)
# numbers[0]=10
# print(f'{len(numbers)} len')
# print(numbers)
# for i in numbers:
#     i *= 2
#     print(i)
# print(numbers) 

# my_list = []  # как добавить 5 элементов в список
# for i in range(5):
#     x = int(input('-->'))
#     my_list.append(x)
# print(my_list)

# my_list = [5, 2, 9, 3, 5, 1, 3] # распечатать все элементы массива с использованием индексов
# for i in range(len(my_list)):
#     print(my_list[i])

# my_list = [5, 2, 9, 3, 5, 1, 3]  # распечатать без индексов
# for i in my_list:
#     print(i)


# my_list = [5, 2, 6]
# my_list.pop(1) # удалит элемент с индексом 1
# my_list.remove(6) # удалит цифру 6 , если найдёт её в списке
# print(my_list)


# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return

# arg = 1
# print(f(arg))
# print(type(f(arg)))
