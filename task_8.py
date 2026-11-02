import random
number = random.randint(1, 100)
while True:
    guess = int(input("Угадай число: "))
    if guess < number:
        print("Больше")
    elif guess > number:
        print("Меньше")
    else:
        print("Вы угадали")
        break