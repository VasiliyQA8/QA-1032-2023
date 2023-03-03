money = int(input("Введите сумму: "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
per_cent_l = list(map(float, per_cent.values()))
ТКБ = per_cent_l[0] * money / 100
СКБ = per_cent_l[1] * money / 100
ВТБ = per_cent_l[2] * money / 100
СБЕР = per_cent_l[3] * money / 100
deposit = list(map(round, [ТКБ, СКБ, ВТБ, СБЕР]))
print(deposit)
print("Максимальная сумма, которую вы можете заработать -", max(deposit))
