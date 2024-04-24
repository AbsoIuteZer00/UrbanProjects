class Building:
    """Здание"""
    def __init__(self):
        self.numberOfFloors = int
        self.buildingType = str

    def __eq__(self, other):
        """Сравнение объектов"""
        return self.numberOfFloors == self.buildingType


building = Building()
building.__eq__(1)
