# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
# 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
my_list = []
while True:
    a = input('ENTER')
    if a == 'q':
        break
    else:
        my_list.append(a)
print(my_list)
if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        per = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = per
        i += 2
else:
    i = 0
    while i < len(my_list) - 1:
        per = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = per
        i += 2

print(my_list)
