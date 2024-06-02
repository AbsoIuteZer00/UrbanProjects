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

multiply = lambda x, y: x ** y
print(multiply(2, 5))


def multiply_def(x, y):
    return x ** y


print(multiply_def(2, 5))


class Repeater:
    def __init__(self, value):
        self.value = value

    def __call__(self, n):
        return [self.value] * n


repeat_num = Repeater(10)
print(repeat_num(5))
