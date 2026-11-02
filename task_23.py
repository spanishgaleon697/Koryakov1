income = {}
expenses = {}
print("=== Личный финансовый помощник ===")
count = int(input("Сколько источников дохода? "))
for i in range(count):
    name = input("Название дохода: ")
    amount = float(input("Сумма дохода: "))
    if name in income:
        income[name] = income[name] + amount
    else:
        income[name] = amount
count = int(input("Сколько категорий расходов? "))
for i in range(count):
    name = input("Категория расхода: ")
    amount = float(input("Сумма расхода: "))
    if name in expenses:
        expenses[name] = expenses[name] + amount
    else:
        expenses[name] = amount
total_income = 0
for name in income:
    total_income = total_income + income[name]
total_expenses = 0
for name in expenses:
    total_expenses = total_expenses + expenses[name]
balance = total_income - total_expenses
print("\n=== Доходы ===")
for name in income:
    print(name, "-", income[name], "руб.")
print("Всего доходов:", total_income, "руб.")
print("\n=== Расходы ===")
for name in expenses:
    print(name, "-", expenses[name], "руб.")
print("Всего расходов:", total_expenses, "руб.")
print("Остаток:", balance, "руб.")
if total_income > 0:
    print("Доля расходов от дохода:",
          round(total_expenses / total_income * 100, 2), "%")
if balance > 0:
    savings = balance * 0.2
    print("Рекомендуемые сбережения (20% остатка):", savings, "руб.")
else:
    print("Рекомендация: сократите расходы или увеличьте доход.")
if len(expenses) > 0:
    biggest = ""
    for name in expenses:
        if biggest == "" or expenses[name] > expenses[biggest]:
            biggest = name
    print("Самая затратная категория:", biggest)
    print("Расходы в этой категории:", expenses[biggest], "руб.")
    print("Рекомендация: проверьте, можно ли уменьшить эти расходы.")
print("\n=== Планирование крупной покупки ===")
purchase = float(input("Стоимость покупки: "))
monthly_saving = float(input("Сколько готовы откладывать в месяц? "))
if monthly_saving > 0:
    months = purchase / monthly_saving
    whole_months = int(months)
    if months > whole_months:
        whole_months = whole_months + 1
    print("Для покупки потребуется месяцев:", whole_months)
else:
    print("Укажите сумму, которую можно откладывать каждый месяц.")