num_1 = 1
num_2 = 1
num = int(input('Введите число '))
i = 0
while i < num - 2:
    num_sum = num_1 + num_2
    num_1 = num_2
    num_2 = num_sum
    i = i + 1


print('Значение элемента', num_2)
