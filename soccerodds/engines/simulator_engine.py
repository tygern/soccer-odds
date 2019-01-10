import random
from typing import Dict

from soccerodds import PredictionEngine
from soccerodds.fixtures.fixture import Fixture, Probabilities, Team
from soccerodds.predictions.prediction_evaluator import Outcome

# Based on last year's results
naive_goal_rates = {
    Team("Arsenal"): 74 / 38 / 90,
    Team("Bournemouth"): 45 / 38 / 90,
    Team("Brighton and Hove Albion"): 34 / 38 / 90,
    Team("Burnley"): 36 / 38 / 90,
    Team("Cardiff City"): 31 / 38 / 90,  # WBA's previous total
    Team("Chelsea"): 62 / 38 / 90,
    Team("Crystal Palace"): 45 / 38 / 90,
    Team("Everton"): 44 / 38 / 90,
    Team("Fulham"): 28 / 38 / 90,  # Swansea's previous total
    Team("Huddersfield Town"): 28 / 38 / 90,
    Team("Leicester City"): 56 / 38 / 90,
    Team("Liverpool"): 84 / 38 / 90,
    Team("Manchester City"): 106 / 38 / 90,
    Team("Manchester United"): 68 / 38 / 90,
    Team("Newcastle United"): 39 / 38 / 90,
    Team("Southampton"): 37 / 38 / 90,
    Team("Tottenham Hotspur"): 74 / 38 / 90,
    Team("Watford"): 44 / 38 / 90,
    Team("West Ham United"): 48 / 38 / 90,
    Team("Wolverhampton Wanderers"): 35 / 38 / 90,  # Stoke's previous total
}


class SimulatorEngine(PredictionEngine):
    def __init__(self, goal_rates: Dict[Team, float]) -> None:
        self.__goal_rates = goal_rates

    def predict(self, fixture: Fixture) -> Probabilities:
        results = [self.__simulate(fixture) for _ in range(1000)]

        return Probabilities(
            home=results.count(Outcome.HOME) / 1000,
            away=results.count(Outcome.AWAY) / 1000,
            draw=results.count(Outcome.DRAW) / 1000
        )

    def __simulate(self, fixture: Fixture) -> Outcome:
        home_goal_rate = self.__goal_rates[fixture.home_team]
        away_goal_rate = self.__goal_rates[fixture.away_team]

        home_score = 0
        away_score = 0

        for _ in range(90):
            if random.random() <= home_goal_rate:
                home_score += 1
            if random.random() <= away_goal_rate:
                away_score += 1

        if home_score > away_score:
            return Outcome.HOME
        elif away_score > home_score:
            return Outcome.AWAY
        else:
            return Outcome.DRAW
