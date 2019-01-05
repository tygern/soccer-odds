from dataclasses import dataclass
from enum import Enum
from fractions import Fraction
from typing import List

from soccerodds.fixtures.fixture import Fixture
from soccerodds.predictions.prediction_engine import PredictionEngine


class Result(Enum):
    HOME = "home"
    AWAY = "away"
    DRAW = "draw"


@dataclass
class Match(object):
    fixture: Fixture
    result: Result


class PredictionEvaluator(object):
    def __init__(self, engine: PredictionEngine) -> None:
        self.engine = engine

    def evaluate(self, matches: List[Match]) -> Fraction:
        correct_predictions = sum([self.__is_correct(m) for m in matches])

        return Fraction(correct_predictions, len(matches))

    def __is_correct(self, match: Match) -> bool:
        return self.__predicted_result(match.fixture) == match.result

    def __predicted_result(self, f: Fixture) -> Result:
        p = self.engine.predict(f)

        if p.home >= p.away and p.home >= p.draw:
            return Result.HOME
        elif p.draw > p.away:
            return Result.DRAW
        else:
            return Result.AWAY
