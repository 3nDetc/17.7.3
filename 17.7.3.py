money = int(input('Введите сумму вклада: '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
b = (list(map(float, per_cent.values())))
deposit = [num * money / 100 for num in b]
deposit = (round(v) for v in deposit)
deposit = list(deposit)
print(deposit)

deposit_max = max(deposit)
print('Максимальная сумма: ', deposit_max)