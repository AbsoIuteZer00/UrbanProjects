class House:
    """Пример класса"""
    def __init__(self):
        self.numberOfFloors = 10


house = House()
for i in range(house.numberOfFloors):
    """цикл для перебора этажей"""
    i += 1
    print(f'Текущий этаж равен {i}')
