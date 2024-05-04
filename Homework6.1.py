class Vehicle:
    vehicle_type = 'None'


class Car:
    price = 1000000

    def horse_powers(self):
        horse_powers = 106
        return horse_powers


class Nissan(Car, Vehicle):
    price = 9900000
    vehicle_type = 'Внедорожник'

    def horse_powers(self):
        horse_powers = 450
        return horse_powers


patrol = Nissan()
print(f'Nissan Patrol\nТип кузова: {patrol.vehicle_type} \nЦена: {patrol.price} руб.')
