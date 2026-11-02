def type_check(*types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if len(args) + len(kwargs) != len(types):
                raise TypeError("Неверное количество аргументов")
            position = 0
            for value in args:
                if type(value) != types[position]:
                    raise TypeError("Неверный тип аргумента")
                position = position + 1
            for name in kwargs:
                if type(kwargs[name]) != types[position]:
                    raise TypeError("Неверный тип аргумента")
                position = position + 1
            return func(*args, **kwargs)
        return wrapper
    return decorator
@type_check(int, int)
def add(a, b):
    return a + b
print(add(2, 3))
print(add(a=4, b=5))