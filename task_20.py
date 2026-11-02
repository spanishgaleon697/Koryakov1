def unique_elements(lst):
    result = []
    def find(items):
        for item in items:
            if type(item) == list:
                find(item)
            elif item not in result:
                result.append(item)
    find(lst)
    return result
list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]
print("Уникальные элементы:", unique_elements(list_a))