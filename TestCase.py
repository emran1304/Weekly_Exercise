import unittest
import Football
from Errors import *
from datetime import *


class HumanTest(unittest.TestCase):

    def setUp(self) -> None:
        self.human_1 = Football.Human('ali', 23)

    def test_age(self):
        with self.assertRaises(HumanAgeError):
            self.human_1.age = 901

    def test_name(self):
        self.assertTrue(self.human_1.name.isalpha())


class PlayerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.player_1 = Football.Player('salah', 29, 'cm', 22000, 100)

    def test_age(self):
        with self.assertRaises(PlayerAgeError):
            self.player_1.age = 67

    def test_salary(self):
        with self.assertRaises(PlayerSalaryError):
            self.player_1.salary = -10000

    def test_rate(self):
        with self.assertRaises(PlayerRateError):
            self.player_1.rate = 125


class CoachTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.coach_1 = Football.Coach('Jurgen Kloop', 54, 100000, datetime(2022, 10, 26), datetime(2099, 10, 26))

    def test_age(self):
        with self.assertRaises(CoachAgeError):
            self.coach_1.age = 84

    def test_start_date(self):
        with self.assertRaises(CoachStartDateError):
            self.coach_1.start_date = datetime(2015, 7, 19)


class Team(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.team_1 = Football.Team('FC Liverpool', 500000, score=500)

    def test_member(self):
        self.assertEqual(len(self.team_1.players), 11)

    def test_coch(self):
        self.assertIsNotNone(self.team_1.coach)


if __name__ == '__main__':
    unittest.main()
