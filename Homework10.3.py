import threading
import time
from queue import Queue


class Table:
    """Класс столиков"""
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Cafe:
    """Класс симуляции работы кафе"""
    def __init__(self, tables_):
        self.queue = Queue()
        self.tables = tables_

    def customer_arrival(self):
        customer_number = 1
        while customer_number <= 20:
            print(f"Посетитель №{customer_number} прибыл.")
            customer_thread = Customer(customer_number, self)
            customer_thread.start()
            customer_number += 1
            time.sleep(1)
            self.queue.put(customer_number)

    def serve_customer(self, customer):
        table_found = False
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f"Посетитель №{customer.number} сел за столик №{table.number}.")
                time.sleep(5)
                table.is_busy = False
                print(f"Посетитель №{customer.number} покушал и ушёл.")
                table_found = True
                break
        if not table_found:
            print(f"Посетитель №{customer.number} ожидает свободный стол.")

            self.queue.put(customer)
            self.queue.get(customer)


class Customer(threading.Thread):
    """Класс посетителей"""
    def __init__(self, number, cafe_):
        super().__init__()
        self.number = number
        self.cafe = cafe_

    def run(self):
        self.cafe.serve_customer(self)


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
table4 = Table(4)
table5 = Table(5)
tables = [table1, table2, table3, table4, table5]

cafe = Cafe(tables)

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

customer_arrival_thread.join()
