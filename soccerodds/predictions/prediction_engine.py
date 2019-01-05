from abc import ABC, abstractmethod

from soccerodds.fixtures.fixture import Fixture, Probabilities


class PredictionEngine(ABC):
    @abstractmethod
    def predict(self, fixture: Fixture) -> Probabilities:
        pass
