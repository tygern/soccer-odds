from soccerodds.fixtures.fixture import Fixture, Probabilities
from soccerodds.predictions.prediction_engine import PredictionEngine


class HomePredictionEngine(PredictionEngine):
    def predict(self, fixture: Fixture) -> Probabilities:
        return Probabilities(
            home=1,
            away=0,
            draw=0
        )
