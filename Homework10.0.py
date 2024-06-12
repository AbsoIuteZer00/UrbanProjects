import time
from threading import Thread

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def stream(*args):
    for result in args:
        time.sleep(1)
        print(f'{result}')


thread = Thread(target=stream, args=list(numbers))
thread.start()
time.sleep(0.5)
stream(*letter)
thread.join()
