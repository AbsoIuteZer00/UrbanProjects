import time
from threading import Thread


class Knight(Thread):

    def __init__(self, name, skill, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.skill = skill

    def run(self):
        invaders = 100
        day = 0
        while invaders > 0:
            invaders = invaders - self.skill
            day += 1
            time.sleep(1)
            if invaders <= 0:
                return print(f'-------------\n{self.name} оборонял замок {day} дней и одержал победу!\n-------------')
            print(f'{self.name} отбивает атаку. День: {day}. Осталось врагов {invaders}')


knight1 = Knight('Sandro', 12)
knight2 = Knight('Rolland', 17)
knight1.start()
time.sleep(0.5)
knight2.start()
knight1.join()
knight2.join()
