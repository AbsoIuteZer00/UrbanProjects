import random
print('Бинарный поиск')
guess_made = 0
guess = 0
random_num = random.randint(1, 100)
while guess_made < 100:
    if guess < random_num:
        guess = guess + 5
        guess_made += 1
        print(f'Попытка №{guess_made}. Бери немного выше.')
    if guess > random_num:
        guess = guess - 3
        guess_made += 1
        print(f'Попытка №{guess_made}. Бери немного ниже.')
    if guess == random_num:
        guess_made += 1
        break


if guess == random_num:
    print(f"Бинго! Ты угадал. Число которое я загадал {random_num}. Ты уложился")
else:
    print(f'Было близко. Я загадывал число: {random_num}')


#
print(f'----------------- \nФункция sum_range')
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
sum_1 = 0


def sum_range(sum_):
    for i in range(a, b):
        sum_ += i
    print(sum_)


sum_range(sum_1)


#
print(f"----------- \nТреугольник")
x1 = int(input('Введите первое число: '))
y1 = int(input('Введите второе число: '))
z1 = int(input('Введите третье число: '))


def triangle(x, y, z):
    if x < y + z and y < x + z and z < x + y:
        print('Трегольник построить возможно')
        if x == y == z:
            print('Этот треугольник равносторонний')
        if x == y != z:
            print('Этот треугольник равнобедренный')
        if x != y != z:
            print('Этот треугольник разностронний')
    else:
        print('Треугольник с такими соронами построить невозможно! Попробуй ещё.')


triangle(x1, y1, z1)


#
print(f'------------------ \nСчастливый билетик')
ticket_ = [int(i) for i in input('Введите номер билета, не более 6 цифр: ')]


def lucky_ticket(ticket):
    if sum(ticket[0:3]) == sum(ticket[3:6]):
        print('Билетик счастливый')
    else:
        print('Билетик не является счастливым')


lucky_ticket(ticket_)
#

print('---------------- \nДлина строки')
string = input('Введите данные для расчёта длины строки: ')
def len_string(string):
    n = 0
    for i in string:
        n += 1
    print(f'Длина строки: {n}')


len_string(string)
