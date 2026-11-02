from datetime import datetime
def log_calls(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(filename, "a", encoding="utf-8") as file:
                file.write("{} | {} | args={} | kwargs={}\n".format(
                    datetime.now(), func.__name__, args, kwargs
                ))
            return func(*args, **kwargs)
        return wrapper
    return decorator
@log_calls("calls.txt")
def add(a, b):
    return a + b
print("Результат функции:", add(2, 3))