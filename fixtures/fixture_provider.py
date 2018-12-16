import json
from typing import Dict, List

from fixtures.fixture import Fixture, Team, Probabilities


class FixtureProvider(object):
    def __init__(self, api_key: str, requests):
        self._requests = requests
        self._api_key = api_key
        self._request_url = "https://api.the-odds-api.com/v3/odds?sport=soccer_epl&region=us&mkt=h2h&apiKey="
        self.bookie = "betfair"

    def upcoming_fixtures(self) -> List[Fixture]:
        response_text = self._requests.get(self._request_url + self._api_key).text
        return [self._dict_to_fixture(d) for d in json.loads(response_text)["data"]]

    def _dict_to_fixture(self, fixture_dict: Dict) -> Fixture:
        home_team_name = fixture_dict["home_team"]
        home_team_index = fixture_dict["teams"].index(home_team_name)
        away_team_name = fixture_dict["teams"][1 - home_team_index]

        odds = [o for o in fixture_dict["sites"] if o["site_key"] == self.bookie][0]["odds"]["h2h"]

        return Fixture(
            home_team=Team(home_team_name),
            away_team=Team(away_team_name),
            probabilities=self._calculate_probabilities(odds, home_team_index),
            start_time=fixture_dict["commence_time"]
        )

    @staticmethod
    def _calculate_probabilities(odds: List[float], home_team_index: int) -> Probabilities:
        harmonic_mean = 1 / sum([1 / o for o in odds])

        return Probabilities(
            home=round(harmonic_mean / odds[home_team_index], 9),
            draw=round(harmonic_mean / odds[2], 9),
            away=round(harmonic_mean / odds[1 - home_team_index], 9)
        )
