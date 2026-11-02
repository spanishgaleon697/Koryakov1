sum = int (input ("Введите сумму: "))
for coin in [100, 50, 10, 5, 2, 1]:
    count = sum // coin
    sum = sum % coin
    print (coin, "руб ", count)