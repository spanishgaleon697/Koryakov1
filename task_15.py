sales = [
    {"name": "Телефон", "price": 20000, "quantity": 3},
    {"name": "Ноутбук", "price": 50000, "quantity": 2},
    {"name": "Телефон", "price": 20000, "quantity": 4},
    {"name": "Наушники", "price": 3000, "quantity": 10}
]
revenue = {}
for sale in sales:
    name = sale["name"]
    total = sale["price"] * sale["quantity"]
    if name in revenue:
        revenue[name] = revenue[name] + total
    else:
        revenue[name] = total
print("Выручка по товарам:")
best_name = ""
best_total = 0
for name in revenue:
    print(name, "-", revenue[name], "руб.")
    if revenue[name] > best_total:
        best_total = revenue[name]
        best_name = name
print("Самый прибыльный товар:", best_name)
print("Количество уникальных наименований:", len(revenue))