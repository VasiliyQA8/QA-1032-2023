price = 0
tickets = int(input("Сколько билетов?\n"))
for i in range(1, tickets + 1):
    age_visitors = int(input('Какой возраст? '))
    if age_visitors >= 18:
        price += 990 if 18 <= age_visitors < 25 else 1390
    else:
        print('Менее 18 лет, то он проходит бесплатно')
discount = price * 10 // 100
price -= discount if tickets > 3 else 0
print(f'Cумма к оплате:  {price} руб.')
