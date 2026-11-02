numbers = [float(x) for x in input("Введите числа через пробел: ").split()]
unique = []
repeated = []
even = []
odd = []
negative = []
decimal = []
multiples = []
for number in numbers:
    count = 0
    for other in numbers:
        if number == other:
            count = count + 1
    if count == 1:
        if number not in unique:
            unique.append(number)
    elif number not in repeated:
        repeated.append(number)
    if number < 0:
        negative.append(number)
    if number == int(number):
        if int(number) % 2 == 0:
            even.append(int(number))
        else:
            odd.append(int(number))
    else:
        decimal.append(number)
    if number % 5 == 0:
        multiples.append(number)
print("Уникальные числа:", unique)
print("Повторяющиеся числа:", repeated)
print("Четные числа:", even)
print("Нечетные числа:", odd)
print("Отрицательные числа:", negative)
print("Числа с плавающей точкой:", decimal)
print("Сумма чисел, кратных 5:", sum(multiples))
print("Максимальное число:", max(numbers))
print("Минимальное число:", min(numbers))