goods = []
while input("Вводим товары ? Enter y/n: ") == 'y':
    number = int(input("Введите номер товара: "))
    features = {}
    while input("Хотите ввести параметры? Enter y/n: ") == 'y':
        feature_key = input("Введите спецификацию: ")
        feature_value = input("Введите значение: ")
        features[feature_key] = feature_value
    goods.append(tuple([number, features]))
print(goods)
analitics = {}
for good in goods:
    for feature_key, feature_value in good[1].items():
        if feature_key in analitics:
            analitics[feature_key].append(feature_value)
        else:
            analitics[feature_key] = [feature_value]
print(analitics)
