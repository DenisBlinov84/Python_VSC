# ВКЛЮЧЕНИЯ:
# my_str = '1 22 54 76 2'
# print(my_str)
# my_list = '1 22 54 76 2'.split()
# print(my_list)
# for i in range(len (my_list)):
#     my_list[i] = int(my_list[i])
# print(my_list)

# Сокращённая запись:
# my_str = '1 22 54 76 2'.split()
# my_str = '1, 22, 54, 76, 2' .split(',')
# my_list = [int(item) for item in my_str] # item-переменная само число, если индекс то i обычно используют
# print(my_list)



# lambda:
# f = lambda x: x**2 if x>10 else x**3
# print(f(12))



# map:
# f = lambda x: x**2 if x>10 else x**3
# my_list = [12, 54, 3, 65]

# res = list(map(f, my_list)) # вместо list можно указать tuple к примеру
# print(res)



# filter:
# f = lambda x: True if x>10 else False
# my_list = [12, 54, 3, 65]
# res = list(filter(f, my_list)) 
# print(res)



# map:
# my_list_1 = [12, 54, 3, 65]
# my_list_2 = [15, 76, 1, 98]
# my_list_3 = [65, 68, 8, 23]
# res = list(zip(my_list_1, my_list_2, my_list_3))
# print(res)

my_list_1 = ['A', 'B', 'C', 'D']
my_list_2 = [15, 76, 1, 98]
res = dict(zip(my_list_1, my_list_2))
print(res)









