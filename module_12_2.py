from runner import Runner
from runner import Tournament
from unittest import TestCase


class TournamentTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        # Бегун по имени Усэйн, со скоростью 10.
        # Бегун по имени Андрей, со скоростью 9.
        # Бегун по имени Ник, со скоростью 3.
        self.var1 = Runner("Усэйн", 10)
        self.var2 = Runner("Андрей", 9)
        self.var3 = Runner("Ник", 3)

    def test_1(self):
        tournament1 = Tournament(90, self.var1, self.var3)
        res1 = tournament1.start()
        TournamentTest.all_results.append(res1)
        self.assertTrue(res1[max(res1)] == 'Ник')

    def test_2(self):
        tournament2 = Tournament(90, self.var2, self.var3)
        res2 = tournament2.start()
        TournamentTest.all_results.append(res2)
        self.assertTrue(res2[max(res2)] == 'Ник')

    def test_3(self):
        tournament3 = Tournament(90, self.var1, self.var2, self.var3)
        res3 = tournament3.start()
        TournamentTest.all_results.append(res3)
        self.assertTrue(res3[max(res3)] == 'Ник')

    @classmethod
    def tearDownClass(cls):
        for k, v in enumerate(cls.all_results, start=1):
            print(f'{k}:{v}')


if __name__ == "__main__":
    unittest.main