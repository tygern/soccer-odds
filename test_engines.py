from soccerodds import CsvMatchPredictionEvaluator
from soccerodds.engines.home_prediction_engine import HomePredictionEngine
from soccerodds.engines.odds_prediction_engine import OddsPredictionEngine

evaluator = CsvMatchPredictionEvaluator("epl-2018.csv")

print(f"Home Engine accuracy: {float(evaluator.evaluate(HomePredictionEngine()))}")
print(f"Odds Engine accuracy: {float(evaluator.evaluate(OddsPredictionEngine()))}")
