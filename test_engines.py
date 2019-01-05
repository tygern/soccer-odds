from soccerodds import evaluate
from soccerodds.engines.home_prediction_engine import HomePredictionEngine
from soccerodds.engines.odds_prediction_engine import OddsPredictionEngine

print(f"Home Engine accuracy: {float(evaluate(HomePredictionEngine()))}")
print(f"Odds Engine accuracy: {float(evaluate(OddsPredictionEngine()))}")
