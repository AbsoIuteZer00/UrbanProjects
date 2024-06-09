def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        n = 0
        for i in range(2, result // 2 + 1):
            if result % i == 0:
                n += 1
        if n <= 0:
            print("Число простое")
        else:
            print("Число составное")
    return wrapper


@is_prime
def sum_three(a, b, c):
    sum_ = a + b + c
    print(sum_)
    return sum_


k = sum_three(2, 5, 10)
