from runner import Runner
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        var1 = Runner("Alex")
        for i in range(10):
            var1.walk()
        self.assertEqual(var1.distance,50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        var2 = Runner("Bob")
        for i in range(10):
            var2.run()
        self.assertEqual(var2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        var1 = Runner("Alex")
        var2 = Runner("Bob")
        for i in range(10):
            var1.walk()
            var2.run()
        self.assertNotEqual(var1.distance, var2.distance)

if __name__ == "__main__":
    unittest.main



