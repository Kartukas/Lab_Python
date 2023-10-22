money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
month = 1
Budget = money_capital + salary - spend
while spend <= Budget + salary:
    month += 1
    spend += spend * increase
    Budget = Budget + salary - spend
    #print(Budget," ", spend)
print("Количество месяцев, которое можно протянуть без долгов:", month)
