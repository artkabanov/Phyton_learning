# словарь с распределением процентных ставок по вкладам в различных банках
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

# ввод суммы с проверкой на ввод чисел
while True:
    money = input("Введите сумму вклада в рублях: ")
    if not money.isnumeric():
        print("Это не число. Попробуйте снова.")
    else:
        print("Молодцом! Вы справились!\n")
        break

# преобразуем ключи и значения словаря в списки
bank = list(per_cent.keys())
deposit = list(per_cent.values())

# пока i меньше длины словаря, заменяем в списке deposit процентную ставку на годовую прибыль от суммы вклада
i = 0
while i < len(per_cent):
    deposit[i] = int(deposit[i]) * int(money) / 100
    print("Прибыль в банке", bank[i],"за год составит", deposit[i], "руб.")
    i += 1

# определяем порядковый номер максимального значения и соответствующий банк
counts = deposit.index(max(deposit))
best_bank = bank[counts]
max_deposit = deposit[counts]

# вывод годовой прибыли по всем банкам, максимальное значение и банк
print(deposit)
print("\nМаксимальная сумма, которую вы можете заработать -", max_deposit, "руб. в банке", best_bank)
