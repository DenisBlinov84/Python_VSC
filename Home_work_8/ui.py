from logger import input_data, print_data, put_data, delete_data


def interface():
    print('Выберите номер варианта:\n'
          '1. Записать данные(в 2-ух форматах)\n'
          '2. Удалить данные\n'
          '3. Изменить данные\n'
          '4. Вывести данные\n')
    command = int(input("Введите номер операции: "))

    while command < 1 or command > 4:
        print('Всего есть четыре варианта: 1, 2, 3 или 4')
        command = int(input("Введите номер операции: "))

    if command == 1:
        input_data()
    elif command == 2:
        delete_data()
    elif command == 3:
        put_data()
    else:
        print_data()




