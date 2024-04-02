def test(*args, **kwargs):
    print('Произвольное число параметров')
    print('args', type(args))
    print(args)
    for i, arg in enumerate(args):
        print('Позиционный параметр', i, arg)
    print('kwargs', type(kwargs))
    for key, value in kwargs.items():
        print('Именованный параметр', key, value)


test(12, 43, 54, 'string', True, a=121, b=144, c=169)
#
print('------------------- \n''Рекурсивная функция')


def recursive_factorial(num_):
    if num_ == 1:
        return 1
    else:
        return num_ * recursive_factorial(num_ - 1)


print(recursive_factorial(5))
