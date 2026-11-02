import time
def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Время выполнения: {:.3f} мс".format((end - start) * 1000))
        return result
    return wrapper
@timing
def calculate():
    result = 0
    for number in range(100000):
        result = result + number
    return result
print("Результат:", calculate())