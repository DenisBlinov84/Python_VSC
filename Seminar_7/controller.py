import oper
import data
from view import view_data
from init import input_data
from logging import logg


def btm():
    logg()
    num_data = (int(input_data('Первое число: ')),
                int(input_data('Второе число: ')))
    logg(head='00', body=f'Enter numbers: {num_data}')            
    data.init_data(*num_data) # распаковываем кортеж
    znak = input_data('Укажите действие: ')
    logg(head='00', body=f'Enter znak: {znak}')
    match znak:
        case '+':
            res =  oper.sum(*data.return_data())
        case '-':
            res = oper.dev(*data.return_data())
        case '*':
            res = oper.mult(*data.return_data())
        case '/':
            res = oper.sub(*data.return_data())
        case _:
            res = 'NONE'

log(head='00', body=f'Get result: {res}')
view_data(text='Результат: ', data = res) 
logg(body='End program')