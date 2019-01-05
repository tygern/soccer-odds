from soccerodds.fixtures.fixture import Fixture, Probabilities
from soccerodds.predictions.prediction_engine import PredictionEngine


class OddsPredictionEngine(PredictionEngine):
    def predict(self, fixture: Fixture) -> Probabilities:
        return fixture.odds.to_probabilities()
