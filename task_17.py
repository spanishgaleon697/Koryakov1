def merge_value(a, b):
    if type(a) == dict and type(b) == dict:
        merge_dicts(a, b)
        return a
    elif type(a) == list and type(b) == list:
        for i in range(len(b)):
            if i < len(a):
                a[i] = merge_value(a[i], b[i])
            else:
                a.append(b[i])
        return a
    elif type(a) == set and type(b) == set:
        return set(list(a) + list(b))
    elif type(a) == tuple and type(b) == tuple:
        result = a
        for item in b:
            if item not in result:
                result = result + (item,)
        return result
    else:
        return b
def merge_dicts(a, b):
    for key in b:
        if key in a:
            a[key] = merge_value(a[key], b[key])
        else:
            a[key] = b[key]
dict_a = {"a": 1, "b": {"c": 1, "f": 4},
          "numbers": [1, 2], "letters": {"a", "b"}, "data": (1, 2)}
dict_b = {"d": 1, "b": {"c": 2, "e": 3},
          "numbers": [3, 4], "letters": {"b", "c"}, "data": (2, 3)}
merge_dicts(dict_a, dict_b)
print("Результат слияния:", dict_a)