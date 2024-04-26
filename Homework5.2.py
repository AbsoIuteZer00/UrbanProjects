class Building:
    """Здание"""
    def __init__(self):
        self.numberOfFloors = 0
        self.buildingType = ''

    def __eq__(self, other):
        """Сравнение объектов"""
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


building_ = Building()
building_2 = Building()
if Building.__eq__(building_, building_2):
    print('Здания идентичны')
