# r (read) -чтение
# w (write) - запись, создаёт новый если нет по указанному пути
# a (append) - дозапись, создаёт новый если нет по указанному пути

# f = open('file.txt', 'w') # file.text-путь, w-режим

# r - сырые строки, чтобы воспринимал как просто быквы без команд

# file_path = r'Seminar_4\file.txt' # Создаём файл-file.txt в папке Seminar_4
# f = open(file_path, 'w')
# f.close()

# file_path = r'Seminar_4\file.txt' # Прочитает содержимое файла -file.txt в папке Seminar_4
# f = open(file_path, 'r')
# print(f.read())  # print(f.read(3))-Считает только 3 символа
# f.close()

# file_path = r'Seminar_4\file.txt' 
# f = open(file_path, 'r')
# for line in f:   # Будет считывать всё построчно и не будет забивать память(интерируемый объект)
#     print(line, end='') # end=''-чтобы print не добавлял пустую строку
# f.close()    

# file_path = r'Seminar_4\file.txt' 
# f = open(file_path, 'w') # Если файл не существует, то создаст его
# f.write('asd')  # Если существует, то затрёт старый и запишет новую информацию
# f.close()

# file_path = r'Seminar_4\file.txt' 
# f = open(file_path, 'a') # Если файл не существует, то создаст его
# f.write('7657')  # Добавит в строку где стоит курсор
# f.write('12345\n') # Добавит в новую строку
# f.close()

# file_path = r'Seminar_4\file.txt'  
# with open(file_path, 'w') as f:   # Сокращённая запись
#     f.write('Hello')  









