import csv
from datetime import datetime
from fractions import Fraction
from typing import List

from soccerodds.fixtures.fixture import Fixture, Odds, Team
from soccerodds.predictions.prediction_engine import PredictionEngine
from soccerodds.predictions.prediction_evaluator import PredictionEvaluator, Result, result_from_string


class CsvMatchPredictionEvaluator(object):

    def __init__(self, filename: str = "epl-2018.csv") -> None:
        self.filename = filename

    def evaluate(self, engine: PredictionEngine) -> Fraction:
        results: List[Result] = []

        with open(self.filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                results.append(Result(
                    fixture=Fixture(
                        home_team=Team(row[1]),
                        away_team=Team(row[2]),
                        odds=Odds(
                            home=float(row[4]),
                            draw=float(row[5]),
                            away=float(row[6])
                        ),
                        start_time=int(datetime.strptime(row[0], "%d/%m/%Y").timestamp())
                    ),
                    outcome=result_from_string(row[3])
                )
                )

        return PredictionEvaluator(engine).evaluate(results)
