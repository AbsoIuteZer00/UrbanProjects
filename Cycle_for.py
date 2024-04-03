print('Таблица умножения')
multiplier = int(input('Введите множитель: '))
for i in range(11):
    if i != 0:
        print(f'{multiplier} * {i} = {multiplier * i}')


#
print('Сумма ряда')
n = int(input('Введите число: '))
sum_ = 0
for i in range(n + 1):
    sum_ += i


print(sum_)
