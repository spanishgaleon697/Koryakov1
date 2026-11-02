def cache(func):
    results = {}
    def wrapper(*args):
        if args not in results:
            results[args] = func(*args)
        else:
            print("Результат взят из кэша")
        return results[args]
    return wrapper
@cache
def square(number):
    print("Выполняется вычисление")
    return number * number
print(square(5))
print(square(5))
print(square(3))