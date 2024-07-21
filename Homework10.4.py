import multiprocessing


class WarehouseManager:
    """Создаём класс менеджера склада и пустой словарь в нём"""
    def __init__(self):
        self.data = {}

    def process_request(self, request):
        """Функция работы логики запросов"""
        product, action, quantity = request
        if action == 'receipt':
            if product in self.data:
                self.data[product] += quantity
            else:
                self.data[product] = quantity
        elif action == 'shipment':
            if product in self.data and self.data[product] <= quantity:
                self.data[product] -= quantity

    def run(self, requests_):
        """Функция запуска программы, в том числе в многопоточности"""
        for request in requests_:
            self.process_request(request)
        with multiprocessing.Pool(processes=2) as pool:
            pool.map(self.process_request, requests_)


if __name__ == '__main__':
    manager = WarehouseManager()
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    manager.run(requests)
    print(manager.data)
