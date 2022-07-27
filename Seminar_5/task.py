# Задача 1
# Дана строка. Нужно удалить слова, в которых встречается сочетание подряд букв 'абв'.
# Вернуть строку 
# 'Привет, мир! Мы очабв любим Пайтонабв! Семинары'

# str_list = 'Привет, мир! Мы очабв любим Пайтонабв! Семинары'

# def strs(str):
#     for item in str_list:
#         if 'абв' in item:
#             str_list.remove(item)
#     print(str_list)
# strs(str_list)    

# Сокращённая форма1
# res = list(filter(lambda item: 'абв' not in item, str_list.split()))
# print(res)

# Сокращённая форма2
# my_str = 'Привет, мир! Мы очабв любим Пайтонабв! Семинары'
# # Берём слово, проверяем из набора, если нет в нём 'абв'
# res = [word for word in my_str.split() if 'абв' not in word]
# print(res)
# print(' '.join(res)) # Переведёт наш список в строку через пробел ' '



