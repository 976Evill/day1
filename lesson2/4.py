# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
#  Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

a = input('ВВедите строку:')
b = a.split(' ')
n = 1
for i in b:
    print(n, i[0:10])
    n += 1
