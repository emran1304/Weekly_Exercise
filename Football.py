from random import randint, choice
from datetime import datetime
from typing import Literal

from faker import Faker
from Loggign import setup_logger
from Errors import *


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if Human.age_validator(1, 100, age):
            self._age = age
        else:
            raise HumanAgeError("Invalid age!")

    @staticmethod
    def age_validator(min, max, age):
        if min <= age <= max:
            return True

        return False

# h1 = Human('a', 50)
# print(h1.__dict__)

class Player(Human):
    def __init__(self, name, age, post: Literal['gk', 'lb', 'cb', 'rb', 'cb', 'dmf', 'cm', 'cm', 'acm', 'st', 'cf'], salary, rate=0):
        super().__init__(name, age)
        self.post = post
        self.salary = salary
        self.rate = rate

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if Human.age_validator(15, 30, age):
            self._age = age
        else:
            raise PlayerAgeError("Invalid age")

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, rate):
        if 0 <= rate <= 100:
            self._rate = rate
        else:
            raise PlayerRateError("Invalid rate!")

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if 0 <= salary:
            self._salary = salary
        else:
            raise PlayerSalaryError("Invalid salary!")

#p1 = Player('salah', 29, 'cm', 22000, 100)

class Coach(Human):

    def __init__(self, name, age, salary, start_date, end_date):
        super().__init__(name, age)
        self.salary = salary
        self.start_date = start_date
        self.end_date = end_date

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if Human.age_validator(30, 65, age):
            self._age = age
        else:
            raise CoachAgeError("Invalid age!")

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if start_date >= datetime.now():
            self._start_date = start_date
        else:
            raise CoachStartDateError("Invalid start_date!")

c1 = Coach('Jurgen Kloop', 54, 100000, datetime(2022, 10, 26), datetime(2099, 10, 26))

class Team:
    def __init__(self, name, balance, score=0):
        self.name = name
        self.balance = balance
        self.score = score
        self.players = Team.people_data_genrator(11)
        faker = Faker()
        self.coach = Coach(faker.name(), randint(30, 60), randint(10000, 5000000), datetime(2022, 10, 1), datetime(2027, 10 ,1))

    @staticmethod
    def people_data_genrator(x):
        fake = Faker()
        people_data = {}

        for i in range(x):
            posts = ['gk', 'lb', 'cb', 'rb', 'cb', 'dmf', 'cm', 'cm', 'acm', 'st', 'cf']
            name = fake.name()
            player = Player(name, randint(15, 30), posts.pop(), randint(30000, 60000), randint(0, 100))
            people_data[name] = player

        return people_data

    def transfer_player(self, other, name):
        if self.balance >= other.players[name].salary:
            self.players[name] = other.players[name]
            transfered_player = other.players.pop(name)
            fake = Faker()
            name = fake.name()
            other.players[name] = Player(name, randint(15, 30), transfered_player.post, randint(3000, 6000),
                                         randint(0, 100))
            for k, v in self.players.items():
                if v.post == transfered_player.post and v.name != transfered_player.name:
                    self.players.pop(k)

    def __gt__(self, other):
        return self.score > other.score

    def __lt__(self, other):
        return self.score > other.score

t1 = Team('FC Liverpool', 500000, score= 500)

class League:
    def __init__(self, name):
        self.name = name
        self.teams = self.__class__.create_teams(5)

    @staticmethod
    def create_teams(x):
        team_generator = {}
        fake = Faker()
        for i in range(x):
            team_name = fake.name.split(' ')[0]
            team_generator[team_name] = Team(team_name, randint(100000, 1000000))

        return team_generator

    def create_match(self):

        result = ['win', 'equal']

        for k in self.teams:
            for i in self.teams:
                if k != i:
                    res = choice(result)
                    if res == 'win':
                        k.score += 3
                    else:
                        k.score += 1
                        i.score += 1

    def show_table(self):

        return sorted(self.teams, key=lambda x: x.score)


logger_league = setup_logger('league', 'league_logfile.log')
logger_team = setup_logger('team', 'team_logfile.log')
logger_transfer = setup_logger('transfer', 'transfer_logfile.log')
logger_class_error = setup_logger('class_error', 'class_error_logfile.log')
