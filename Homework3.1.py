def print_params(a=1, b='string', c=True):
    print(a, b, c)


print_params()
print_params(1, 'string')
print_params('string')  # PyCharm предупреждает о присвоении ожидаемому параметру int, значение str
print_params(b=25)  # PyCharm предупреждает о присвоении ожидаемому параметру str, значение int
print_params(c=[5, 10, 15])  # PyCharm предупреждает о присвоении ожидаемому параметру bool, значение list

values_list = [12, 'str', True]
values_dict = {'a': 5, 'b': 'str', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [27, 'str']
print_params(*values_list_2, 42)  # PyCharm передал значения из списка параметру 'a' и 'b'. Несмотря на то, что
# PyCharm подсказывает в вызове функции, что число 42 передано к параметру 'a', оно передано параметру 'c'.
