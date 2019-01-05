from soccerodds import CsvMatchPredictionEvaluator
from soccerodds.engines.home_prediction_engine import HomePredictionEngine
from soccerodds.engines.odds_prediction_engine import OddsPredictionEngine
from soccerodds.engines.simulator_engine import SimulatorEngine, naive_goal_rates


evaluator = CsvMatchPredictionEvaluator("epl-2018.csv")

print(f"Home Engine accuracy: {float(evaluator.evaluate(HomePredictionEngine()))}")
print(f"Odds Engine accuracy: {float(evaluator.evaluate(OddsPredictionEngine()))}")
print(f"Simulator Engine accuracy: {float(evaluator.evaluate(SimulatorEngine(naive_goal_rates)))}")
