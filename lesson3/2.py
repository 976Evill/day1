# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

# # именованные параметры
# def second_func(var_2, var_1, var_3):
#     print(f"var_2 - {var_2}; var_1 - {var_1}; var_3 - {var_2}")
#
# second_func(var_1=10, var_2=20, var_3=30))
def user(name, surname, date_born, city, email, tel):
    print(
        f"имя-{name}; фамилия -{surname};день рождения-{date_born};город проживания-{city}; email-{email}; телефон-{tel}")


a = input('Введите фамилию:')
b = input('Введитье имя:')
c = input('Введите день рождения:')
d = input('Введите город:')
e = input('введите email:')
f = input('Введите tel:')
user(tel=f, city=d, email=e, name=b, date_born=c, surname=a)
