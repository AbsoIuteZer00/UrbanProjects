class ByZero(Exception):
    def __init__(self, message, info):
        self.message = message
        self.info = info


class ErrorType(Exception):
    def __init__(self, message, info):
        self.message = message
        self.info = info


def function_(a, b):
    if b == 0:
        raise ByZero('Нельзя делить на ноль', {'a': a, 'b': b})
    if a != int() or b != int():
        raise ErrorType('Неправильный тип данных.', {'a': a, 'b': b})
    return a / b


try:
    result_1 = function_(12, 0)
except ByZero as e:
    print(f'Обнаружена ошибка! \nСообщение об ошибке: {e.message} \nДополнительная ифнормация: {e.info}')
try:
    result_2 = function_(13, '6')
except ErrorType as exc:
    print(f'Обнаружена ошибка! \nСообщение об ошибке: {exc.message} \nДополнительная ифнормация: {exc.info}')
