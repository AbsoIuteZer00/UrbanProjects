class House:
    """Пример класса"""
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print('Текущий этаж:', self.numberOfFloors)


house = House()
house.setNewNumberOfFloors(15)
