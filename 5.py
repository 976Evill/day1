# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
a = float(input('Введите выручку: '))
b = float(input('ВВедите затраты: '))
if a > b:
    print('Прибыль')
    rent = (a - b) / a
    print(f"Рентабельность: {rent:.2f}")
    sotrudniku = int(input('Введите количество сотрудников : '))
    # print('На каждого прибыль = ',"%.2f" (a - b) / (sotrudniku))
    print(f"На каждого прибыль: {(a - b) / sotrudniku:.2f}")


else:
    print('Убыток')
