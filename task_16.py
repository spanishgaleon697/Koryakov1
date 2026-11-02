def flatten_list(lst):
    i = 0
    while i < len(lst):
        if type(lst[i]) == list:
            nested = lst[i]
            flatten_list(nested)
            lst[i:i + 1] = nested
            i = i + len(nested)
        else:
            i = i + 1
list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
flatten_list(list_a)
print("Плоский список:", list_a)