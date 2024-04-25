class Building:
    total = 0

    def __init__(self):
        Building.total += 1


building_size = 40
while Building.total < building_size:
    building = Building()
    print(Building.total)
