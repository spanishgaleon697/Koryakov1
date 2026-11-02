text = input("Введите текст: ").lower()
words = text.split()
for step in range(2):
    if step == 1:
        words = [word for word in words if len(word) >= 3]
    print("\nКоличество слов:", len(words))
    frequency = {}
    for word in words:
        word = word.strip(".,!?;:-()\"'")
        if word != "":
            frequency[word] = frequency.get(word, 0) + 1
    if len(frequency) > 0:
        most_common = ""
        shortest = ""
        longest = ""
        for word in frequency:
            if frequency[word] > frequency.get(most_common, 0):
                most_common = word
            if shortest == "" or len(word) < len(shortest):
                shortest = word
            if len(word) > len(longest):
                longest = word
        print("Частота слов:", frequency)
        print("Самое частое слово:", most_common)
        print("Самое короткое слово:", shortest)
        print("Самое длинное слово:", longest)