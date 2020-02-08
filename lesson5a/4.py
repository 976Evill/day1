# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.
with open("numbers2.txt", "a") as f1:
    with open("numbers.txt", "r") as f:
        for line in f:
            sp = line.split(' ')
            if sp[0] == 'One':
                sp[0] = 'Один'
                sp1 = (' '.join(sp))
                f1.write(sp1)
            elif sp[0] == 'Two':
                sp[0] = 'Два'
                sp1 = (' '.join(sp))
                f1.write(sp1)
            elif sp[0] == 'Three':
                sp[0] = 'Три'
                sp1 = (' '.join(sp))
                f1.write(sp1)
            elif sp[0] == 'Four':
                sp[0] = 'Четыре'
                sp1 = (' '.join(sp))
                f1.write(sp1)
