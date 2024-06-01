def squaring(x):
    return x ** 2


def multiple(x):
    return x % 2


my_numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
result = map(squaring, filter(multiple, my_numbers))
print(list(result))
