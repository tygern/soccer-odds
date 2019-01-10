from dataclasses import dataclass
from enum import Enum
from fractions import Fraction
from typing import List

from soccerodds.fixtures.fixture import Fixture
from soccerodds.predictions.prediction_engine import PredictionEngine


class Outcome(Enum):
    HOME = "home"
    AWAY = "away"
    DRAW = "draw"


def result_from_string(s: str) -> Outcome:
    return [o for o in Outcome if o.value == s][0]


@dataclass
class Result(object):
    fixture: Fixture
    outcome: Outcome


class PredictionEvaluator(object):
    def __init__(self, engine: PredictionEngine) -> None:
        self.engine = engine

    def evaluate(self, matches: List[Result]) -> Fraction:
        correct_predictions = sum([self.is_correct(m) for m in matches])

        return Fraction(correct_predictions, len(matches))

    def is_correct(self, result: Result) -> bool:
        return self.predicted_outcome(result.fixture) == result.outcome

    def predicted_outcome(self, f: Fixture) -> Outcome:
        p = self.engine.predict(f)

        if p.home >= p.away and p.home >= p.draw:
            return Outcome.HOME
        elif p.draw > p.away:
            return Outcome.DRAW
        else:
            return Outcome.AWAY
