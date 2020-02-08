# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
with open("Nabor.txt", "w") as f:
    while True:
        a = input('Введите числа через пробел: ')
        if len(a) == 0:
            break
        else:
            f.write(a + '\n')
with open("Nabor.txt", "r") as f:
    for line in f:
        summ = 0
        b = line.split(' ')
        num = [int(i) for i in b]
        summ += sum(num)
        print(summ)
