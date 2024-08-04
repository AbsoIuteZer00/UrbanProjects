import unittest
import test_runner_12_2
import test_tournament_12_2

runnerST = unittest.TestSuite()
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_runner_12_2.RunnerTest))
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_tournament_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runnerST)
