# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.
N = input('Ведите число n :')

S = int(N) + int(N + N) + int(N + N + N)
print(S)
