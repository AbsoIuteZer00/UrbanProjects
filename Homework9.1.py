print(f'Задача №1: Фабрика функций')


def function_(operation):
    if operation == "sum_":
        def sum_(a, b):
            return a + b

        return sum_
    elif operation == "difference":
        def difference(a, b):
            return a - b

        return difference


my_function = function_("sum_")
print(my_function(10, 5))

print(f'Задача №2: Лямбда')
multiply = (lambda x, y: x ** y)
print(multiply(2, 5))


def multiply_def(x, y):
    return x ** y


print(multiply_def(2, 5))


print(f'Задача №3: Вызываемые объекты')


class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self):
        return self.x * self.y


square_num = Square(5, 3)
print(square_num.__call__())
