salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
grow = increase + 1
money_ = 0  # количество денег, чтобы прожить 10 месяцев
delta = salary - spend

# TODO Оформить решение
for money in range(1, months +1):
    money = spend - salary
    spend = spend * grow
    money_ += money
print(round(money_))