from soccerodds.engines.simulator_engine import SimulatorEngine
from soccerodds.fixtures.fixture import Team, Fixture, Odds, Probabilities

winners = Team("Winners")
losers = Team("Losers")
good = Team("Good")
ok = Team("OK")

goal_rates = {
    winners: 1,
    losers: 0,
    ok: .02,
    good: .03
}


def test_predict():
    engine = SimulatorEngine(goal_rates)

    result = engine.predict(Fixture(
        home_team=winners,
        away_team=losers,
        start_time=0,
        odds=Odds(home=1, away=1, draw=1)
    ))

    assert result == Probabilities(
        home=1,
        away=0,
        draw=0
    )


def test_predict_closer():
    engine = SimulatorEngine(goal_rates)

    result = engine.predict(Fixture(
        home_team=ok,
        away_team=good,
        start_time=0,
        odds=Odds(home=1, away=1, draw=1)
    ))

    assert .2 < result.home < .3
    assert .1 < result.draw < .2
    assert .55 < result.away < .65

    assert .95 < result.home + result.draw + result.away < 1.05
