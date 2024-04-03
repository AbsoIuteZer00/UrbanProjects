import math
import random
print('Поиск простых чисел')
num = int(input('Введите число: '))
primes = [2]
num_test = 3
while num_test < num:
    n = 0
    while primes[n] <= math.sqrt(num_test):
        if (num_test % primes[n]) == 0:
            num_test += 1
            break
        else:
            n += 1
    else:
        primes.append(num_test)
        num_test += 1
print('Простые числа:', primes)


#
print('-------------------\n''Игра "Угадай число"')
name = input('Как тебя зовут? ')
gueses_made = 0
random_num = random.randint(1, 100)
print(f'Посмотрим, насколько ты удачлив. Я загадал число от 0 до 100, у тебя есть 10 попыток. Удачи, {name}!')
while gueses_made < 10:
    guess = int(input('Введи число: '))
    gueses_made += 1
    if guess < random_num:
        print('Бери немного выше')
    if guess > random_num:
        print('Бери немного ниже')
    if guess == random_num:
        break
if guess == random_num:
    print(f'Бинго! {name}, ты лучший! Я загадал число {random_num}!')
else:
    print(f'Было близко... На самом деле, нет. Я загадывал {random_num}. В следующий раз удача тебя не подведёт! Но это'
          f' не точно! :)')
