import task
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner_1 = task.Runner(name='Чип')
        for _ in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    def test_run(self):
        runner_2 = task.Runner(name='Дейл')
        for _ in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    def test_challenge(self):
        runner_1 = task.Runner(name='Чип')
        runner_2 = task.Runner(name='Дейл')
        for _ in range(10):
            runner_1.walk()
            runner_2.run()
        self.assertNotEqual(runner_1.distance, runner_2.distance)
