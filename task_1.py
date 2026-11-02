fio = input("Введите фамилию, имя и отчество: ")
parts = fio.split()
surname = parts[0]
name = parts[1]
otch = parts[2]
result = surname + " " + name[0] + "." + otch[0] + "."
print(result)