a = input("Введите первый набор чисел через пробел: ").split()
b = input("Введите второй набор чисел через пробел: ").split()
common = []
only_a = []
only_b = []
different = []
for number in a:
    if number in b and number not in common:
        common.append(number)
    if number not in b and number not in only_a:
        only_a.append(number)
for number in b:
    if number not in a and number not in only_b:
        only_b.append(number)
for number in a:
    if number not in common and number not in different:
        different.append(number)
for number in b:
    if number not in common and number not in different:
        different.append(number)
print("Общие числа:", common)
print("Только в первом наборе:", only_a)
print("Только во втором наборе:", only_b)
print("Числа из обоих наборов без общих:", different)