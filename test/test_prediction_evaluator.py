from fractions import Fraction

from soccerodds.fixtures.fixture import Odds, Team, Fixture
from soccerodds.engines.home_prediction_engine import HomePredictionEngine
from soccerodds.predictions.prediction_evaluator import Outcome, Result, PredictionEvaluator


def test_evaluate():
    matches = [
        Result(
            fixture=Fixture(
                home_team=Team("Chelsea"),
                away_team=Team("Swansea"),
                odds=Odds(home=1.48, draw=4.6, away=7.55),
                start_time=1544967000),
            outcome=Outcome.HOME
        ),
        Result(
            fixture=Fixture(
                home_team=Team("Colorado Rapids"),
                away_team=Team("Kittens"),
                odds=Odds(home=1.95, draw=3.9, away=3.9),
                start_time=1544967000),
            outcome=Outcome.DRAW
        ),
        Result(
            fixture=Fixture(
                home_team=Team("Tottenham"),
                away_team=Team("Just Some Kids"),
                odds=Odds(home=1.95, draw=3.9, away=3.9),
                start_time=1544967000),
            outcome=Outcome.AWAY
        )
    ]

    evaluator = PredictionEvaluator(HomePredictionEngine())

    assert evaluator.evaluate(matches) == Fraction(1, 3)
