import itertools


def all_variants(abc):
    """Принимаем список с помощью функции"""
    my_list = []
    for list_1 in range(1, len(abc) + 1):
        my_list.append(list(itertools.combinations(abc, list_1)))
    for list_2 in my_list:
        for list_3 in list_2:
            if ''.join(list_3) != 'ac':
                yield ''.join(list_3)


a = all_variants("abc")
for i in a:
    print(i)
