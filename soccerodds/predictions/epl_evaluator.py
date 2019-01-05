import csv
from datetime import datetime
from fractions import Fraction
from typing import List

from soccerodds.fixtures.fixture import Fixture, Odds
from soccerodds.predictions.prediction_engine import PredictionEngine
from soccerodds.predictions.prediction_evaluator import PredictionEvaluator, Match, result_from_string


def evaluate(engine: PredictionEngine) -> Fraction:
    matches: List[Match] = []

    with open("epl-2018.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            matches.append(Match(
                fixture=Fixture(
                    home_team=row[1],
                    away_team=row[2],
                    odds=Odds(
                        home=row[4],
                        draw=row[5],
                        away=row[6]
                    ),
                    start_time=int(datetime.strptime(row[0], "%d/%m/%Y").timestamp())
                ),
                result=result_from_string(row[3])
            )
            )

    return PredictionEvaluator(engine).evaluate(matches)
