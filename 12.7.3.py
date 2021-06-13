# словарь с распределением процентных ставок по вкладам в различных банках
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

# ввод суммы
money = int(input("Введите сумму вклада в рублях: "))
#money = 100000
# преобразуем ключи и значения словаря в списки
deposit = list(per_cent.keys())
deposit = list(per_cent.values())

# пока i меньше длины словаря, заменяем в списке deposit процентной ставки на годовую прибыль от вклада
i = 0
while i < len(per_cent) :
    deposit[i] = int(deposit[i]*money/100)
    i = i + 1

# определяем максимальное значение, его порядковый номер и соответствующий банк
max_deposit = max(deposit)
counts = deposit.index(max_deposit)
best_bank = list(per_cent.keys())[counts]

# вывод годовой прибыли по всем банкам, максимальное значение и банк
print(deposit)
print("Максимальная сумма, которую вы можете заработать:", max_deposit, "руб. в банке", best_bank)
