class Team(object):
    def __init__(self, name: str):
        self.name = name

    def __eq__(self, o) -> bool:
        return self.__class__ == o.__class__\
               and self.name == o.name


class Probabilities(object):
    def __init__(self, home: float, draw: float, away: float):
        self.home = home
        self.draw = draw
        self.away = away

    def __eq__(self, o) -> bool:
        return self.__class__ == o.__class__\
               and self.home == o.home\
               and self.draw == o.draw\
               and self.away == o.away


class Fixture(object):
    def __init__(self, home_team: Team, away_team: Team, probabilities: Probabilities, start_time: int):
        self.home_team = home_team
        self.away_team = away_team
        self.probabilities = probabilities
        self.start_time = start_time

    def __eq__(self, o) -> bool:
        return self.__class__ == o.__class__\
               and self.home_team == o.home_team\
               and self.away_team == o.away_team\
               and self.probabilities == o.probabilities\
               and self.start_time == o.start_time
