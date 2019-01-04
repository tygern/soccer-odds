from soccerodds.fixtures.fixture import Probabilities, Odds


def test_to_probabilities():
    probabilities = Odds(home=1.48, draw=4.6, away=7.55).to_probabilities()

    assert probabilities == Probabilities(home=0.658863257, draw=0.211982091, away=0.129154652)
