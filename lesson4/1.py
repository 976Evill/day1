# . Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для
# конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv

script_name, sum_chasov, stavka, premia = argv


def zp(sum_chasov, stavka, premia):
    itog = float(sum_chasov) * float(stavka) + float(premia)
    print('Сумма на руки', itog)


zp(sum_chasov, stavka, premia)
