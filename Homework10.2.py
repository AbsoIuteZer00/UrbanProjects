import threading
import time


class BankAccount:

    def __init__(self, lock):
        self.balance = 10000
        self.balance_lock = lock

    def deposit(self, amount):
        with self.balance_lock:
            self.balance += amount

    def withdraw(self, amount):
        with self.balance_lock:
            self.balance -= amount


def deposit_task(account, amount):
    for _ in range(30):
        account.deposit(amount)
        print(f'Внесено на счёт: {amount}. Новый баланс: {account.balance}')


def withdraw_task(account, amount):
    for _ in range(20):
        time.sleep(0.001)
        account.withdraw(amount)
        print(f'Снято наличных: {amount}. Новый баланс: {account.balance}')


lock_ = threading.Lock()
bank_acc = BankAccount(lock=lock_)
deposit_thread = threading.Thread(target=deposit_task, args=(bank_acc, 120))
withdraw_thread = threading.Thread(target=withdraw_task, args=(bank_acc, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
