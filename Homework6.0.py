class Car:
    price = 1000000

    def horse_powers(self):
        horse_powers = 106
        return horse_powers


class Nissan(Car):
    price = 9900000

    def horse_powers(self):
        horse_powers = 450
        return horse_powers


class Kia(Car):
    price = 5900000

    def horse_powers(self):
        horse_powers = 200
        return horse_powers


patrol = Nissan()
sorento = Kia()
patrol.horse_powers()
sorento.horse_powers()
print(f'Nissan Patrol: {patrol.horse_powers()} лошадинных сил. Цена: {patrol.price} руб.')
print(f'Kia Sorento: {sorento.horse_powers()} лошадинных сил. Цена: {sorento.price} руб.')
