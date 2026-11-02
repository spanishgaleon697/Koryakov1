age = int(input("Возраст заемщика: "))
income = float(input("Ежемесячный доход: "))
credit = float(input("Сумма кредита: "))
months = int(input("Срок кредита в месяцах: "))
history = input("Кредитная история (отличная/хорошая/удовлетворительная/плохая): ")
por = input("Есть поручитель? (да/нет): ")
zalog = input("Есть залог? (да/нет): ")
if income > 0:
    otn = credit / income
else:
    otn = 0
print("Отношение кредита к доходу:", round(otn, 2))
risk = 0
if age < 18 or age > 70:
    risk += 2
if otn > 10:
    risk += 3
elif otn > 6:
    risk += 2
elif otn > 3:
    risk += 1
if history == "плохая":
    risk += 3
elif history == "удовлетворительная":
    risk += 2
elif history == "хорошая":
    risk += 1
if por == "да":
    risk -= 1
if zalog == "да":
    risk -= 1
if months > 60:
    risk += 1
if risk < 0:
    risk = 0
if risk <= 1:
    category = "Низкий"
    rate = 10
    decision = "Рекомендуется одобрить"
elif risk <= 3:
    category = "Средний"
    rate = 15
    decision = "Можно одобрить после проверки"
elif risk <= 5:
    category = "Высокий"
    rate = 20
    decision = "Требуется дополнительная проверка"
else:
    category = "Критический"
    rate = 30
    decision = "Рекомендуется отклонить"
print("Категория риска:", category)
print("Предлагаемая ставка:", rate, "%")
print("Рекомендация:", decision)