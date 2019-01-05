from dataclasses import dataclass


@dataclass(frozen=True)
class Team(object):
    name: str


@dataclass(frozen=True)
class Probabilities(object):
    home: float
    draw: float
    away: float


@dataclass(frozen=True)
class Odds(object):
    home: float
    draw: float
    away: float

    def to_probabilities(self) -> Probabilities:
        harmonic_mean = 1 / (1 / self.home + 1 / self.draw + 1 / self.away)

        return Probabilities(
            home=round(harmonic_mean / self.home, 9),
            draw=round(harmonic_mean / self.draw, 9),
            away=round(harmonic_mean / self.away, 9)
        )


@dataclass(frozen=True)
class Fixture(object):
    home_team: Team
    away_team: Team
    odds: Odds
    start_time: int
