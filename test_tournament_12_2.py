import tournament
import unittest


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        self.runner_1 = tournament.Runner(name='Усейн', speed=10)
        self.runner_2 = tournament.Runner(name='Андрей', speed=9)
        self.runner_3 = tournament.Runner(name='Ник', speed=3)
        self.tour_list_1 = [self.runner_1, self.runner_3]
        self.tour_list_2 = [self.runner_2, self.runner_3]
        self.tour_list_3 = [self.runner_1, self.runner_2, self.runner_3]

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_result.items():
            print(key, value)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_1(self):
        tour_1 = tournament.Tournament(90, *self.tour_list_1)
        tour_1.start()
        result = tour_1.finishers
        self.assertTrue(result[2] == 'Ник')
        self.all_result[1] = result

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_2(self):
        tour_2 = tournament.Tournament(90, *self.tour_list_2)
        tour_2.start()
        result = tour_2.finishers
        self.assertTrue(result[2] == 'Ник')
        self.all_result[2] = result

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_3(self):
        tour_3 = tournament.Tournament(90, *self.tour_list_3)
        tour_3.start()
        result = tour_3.finishers
        self.assertTrue(result[3] == 'Ник')
        self.all_result[3] = result


if __name__ == '__main__':
    unittest.main()
