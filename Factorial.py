import math
print(math.factorial(6))
factorial = 1
num = int(input('Введите число '))
for i in range(1, num + 1):
    factorial *= i
print(factorial)
