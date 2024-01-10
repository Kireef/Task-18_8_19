# Запрос количества билетов
try:
    num_tickets = int(input('Введите количество билетов: '))
    if num_tickets <= 0:
        print('Введите корректное число')
    else:
        total_price = 0

        for i in range(num_tickets):
            age = int(input(f'Введите возраст посетителя {i+1}: '))

            if age < 18:
                ticket_price = 0
            elif 18 <= age < 25:
                ticket_price = 990
            else:
                ticket_price = 1390

            total_price += ticket_price

        # Применение скидки
        if num_tickets > 3:
            total_price *= 0.9

        print(f'Общая стоимость билетов: {total_price:.2f} руб.')

except ValueError:
    print('Ошибка ввода данных')
