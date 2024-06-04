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
my_function = function_("difference")
print(my_function(15, 3))

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
        print(f'Сторона x: {self.x}, Сторона y: {self.y}')
        area = self.x * self.y
        print(f'Площадь: {area}')


square_num = Square(5, 3)
print(square_num())
