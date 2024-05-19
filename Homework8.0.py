def add_everything_up(a, b):
    sum_ = 0

    try:
        sum_ = a + b
    except TypeError:
        print(f'{a}{b}')
    finally:
        if sum_ > 1:
            print(sum_)


add_everything_up(151.96, 'км')
add_everything_up('осталось', 379)
add_everything_up(151.96, 379)
