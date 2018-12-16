from attr import dataclass


@dataclass
class Team(object):
    name: str


@dataclass
class Probabilities(object):
    home: float
    draw: float
    away: float


@dataclass
class Fixture(object):
    home_team: Team
    away_team: Team
    probabilities: Probabilities
    start_time: int
