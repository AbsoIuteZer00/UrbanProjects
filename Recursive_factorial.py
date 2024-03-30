def recursive_factorial(num_):
    if num_ == 1:
        return num_
    else:
        return num_ * recursive_factorial(num_ - 1)


print(recursive_factorial(6))
