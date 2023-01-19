tickets = int(input('Какое кол-во билетов? '))
cost = 0
n = 1   # посетитель №

for i in range(tickets):
    age = int(input(f'Сколько лет {n} поситителю: '))
    if age < 18:
        print('Билет бесплатный')
    elif 18 < age < 25:
        cost += 990
        print(f'Стомость билета: 990 рублей')
    else:
        cost += 1390
        print(f'Стоимость билета: 1390 рублей')
    n += 1

if tickets > 3:
    sale = round(cost - (cost / 100) * 10)
    print(f'Сумма заказа {sale} рублей, применена 10% скидка за покупку более 3 билетов!')
else:
    print(f'Сумма заказа {cost} рублей')