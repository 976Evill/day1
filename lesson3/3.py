# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def my_func(a, b, c):
    list = [a, b, c]
    list.remove(min(list))
    print(sum(list))


a = int(input('Введите а :'))
b = int(input('Введите b :'))
c = int(input('Введите c :'))

my_func(a, b, c)
