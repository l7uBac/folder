from runner import Runner
from unittest import TestCase

class RunnerTest(TestCase):

    def test_walk(self):
        var1 = Runner("Alex")
        for i in range(10):
            var1.walk()
        self.assertEqual(var1.distance,50)

    def test_run(self):
        var2 = Runner("Bob")
        for i in range(10):
            var2.run()
        self.assertEqual(var2.distance, 100)

    def test_challenge(self):
        var1 = Runner("Alex")
        var2 = Runner("Bob")
        for i in range(10):
            var1.walk()
            var2.run()
        self.assertNotEqual(var1.distance, var2.distance)

if __name__ == "__main__":
    unittest.main



