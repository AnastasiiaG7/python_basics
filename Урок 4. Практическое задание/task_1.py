"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
import sys
empl_name, hours_worked, sal_by_hour, extra = sys.argv

def salary(empl_name, hours_worked, sal_by_hour, extra):
    try:
        print(f'Сотрудник{empl_name} заработал {(hours_worked * sal_by_hour) + extra} рублей')
    except:
        print('Произошла ошибка!')
salary('Елена', 20, 300, 1000)