salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03 # Ежемесячный рост цен
capital = 0
for i in range(1, months+1):
    capital += salary
    capital -= spend
    spend = spend + (spend * increase)
capital = int(round(abs(capital), 0))
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", capital)
