from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input("В каком формате Вы хотите записать данные?\n\n"
                    "1 Вариант:\n\n"
                    "Иванов\n"
                    "Иван\n"
                    "+79991111215\n"
                    "г. Вологда ул. Северная д16к1\n\n"
                    "2 Вариант:\n\n"
                    "Иванов;Иван;+79991111215;г. Вологда ул. Северная д16к1\n\n"
                    "Выберите номер варианта: "))

    while var != 1 and var != 2:
        print('Всего есть два варианта: 1 или 2')
        var = int(input("Введите номер варианта: "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{address}\n\n')


def print_data():
    print('Вывожу данные для Вас из 1-ого файла\n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        data_first_version_second = []
        data_middle = ''
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_version_second.append(''.join(data_first[j:i + 1]))
                j = i
        data_first = data_first_version_second
        print(''.join(data_first))
    print('Вывожу данные для Вас из 2-ого файла\n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data_second = list(file.readlines())
        print(*data_second)
    return data_first, data_second


def put_data():
    print('Из какого файла Вы хотите изменить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Всего есть два варианта: 1 или 2')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        number_journal -= 1
        
        print(f'Изменить данную запись\n{data_first[number_journal]}')
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        data_first = data_first[:number_journal] + [f'{name}\n{surname}\n{phone}\n{address}\n'] + \
                     data_first[number_journal + 1:]
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Изменения успешно сохранены!')
    else:
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        number_journal -= 1
        
        print(f'Изменить данную запись\n{data_second[number_journal]}')
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        data_second = data_second[:number_journal] + [f'{name};{surname};{phone};{address}\n'] + \
                      data_second[number_journal + 1:]
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Изменения успешно сохранены!')  


def delete_data():
    print('Из какого файла Вы хотите удалить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
        
        print(f'Удалить данную запись\n{data_first[number_journal - 1]}')
        data_first = data_first[:number_journal] + data_first[number_journal + 1:]
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Изменения успешно сохранены!')
    else:
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
        
        print(f'Удалить данную запись\n{data_second[number_journal - 1]}')
        data_second = data_second[:number_journal] + data_second[number_journal + 1:]
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Изменения успешно сохранены!')  
