price = float(input("Сумма покупки: "))
age = int(input("Возраст покупателя: "))
birthday = bool(input("Сегодня день рождения?: "))
vip = bool(input("Покупатель VIP?: "))
discount = 0
if price > 1000:
    discount += 10
if age >= 63:
    discount += 5
if birthday == True:
    discount += 5
if vip == True and discount < 15:
    discount = 15
if discount > 25:
    discount = 25
final_price = price * (1 - discount / 100)
print("Скидка:", discount, "%")
print(f"К оплате: {final_price:.2f} руб.")