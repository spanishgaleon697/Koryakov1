min = int(input("Количество минут: "))
sms = int(input("Количество SMS: "))
mb = int(input("Количество МБ интернета: "))
bprice = 24.99
extramin = max(0, min - 60) * 0.89
extrasms = max(0, sms - 30) * 0.59
extramb = max(0, mb - 1024) * 0.79
total = bprice + extramin + extrasms + extramb
tax = total * 0.02
total = total + tax
print(f"Базовый тариф: {bprice:.2f} руб.")
if extramin > 0:
    print(f"Дополнительные минуты: {extramin:.2f} руб.")
if extrasms > 0:
    print(f"Дополнительные SMS: {extrasms:.2f} руб.")
if extramb > 0:
    print(f"Дополнительный интернет: {extramb:.2f} руб.")
print(f"Налог 2%: {tax:.2f} руб.")
print(f"Итого к оплате: {total:.2f} руб.")