parol = input("Введите пароль: ")
if len(parol) < 16:
    input("Пароль слишком короткий")
elif parol.isalpha() or parol.isdigit():
    print("Слабый пароль")
else:
    print("Надежный пароль")