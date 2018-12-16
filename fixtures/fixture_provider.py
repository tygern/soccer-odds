import json
from typing import Dict, List

from fixtures.fixture import Fixture, Team, Probabilities


class FixtureProvider(object):
    def __init__(self, api_key: str, requests):
        self._requests = requests
        self._api_key = api_key
        self._request_url = "https://api.the-odds-api.com/v3/odds?sport=soccer_epl&region=us&mkt=h2h&apiKey="

    def upcoming_fixtures(self) -> List[Fixture]:
        response_text = self._requests.get(self._request_url + self._api_key).text
        return [self._dict_to_fixture(d) for d in json.loads(response_text)["data"]]

    def _dict_to_fixture(self, fixture_dict: Dict) -> Fixture:
        home_team_name = fixture_dict["home_team"]
        away_team_name = [t for t in fixture_dict["teams"] if t != home_team_name][0]
        odds = [o for o in fixture_dict["sites"] if o["site_key"] == "betfair"][0]["odds"]["h2h"]

        return Fixture(
            Team(home_team_name),
            Team(away_team_name),
            self._calculate_probabilities(odds),
            fixture_dict["commence_time"]
        )

    @staticmethod
    def _calculate_probabilities(odds: List[float]) -> Probabilities:
        harmonic_mean = 1 / sum([1 / o for o in odds])

        return Probabilities(
            round(harmonic_mean / odds[0], 9),
            round(harmonic_mean / odds[1], 9),
            round(harmonic_mean / odds[2], 9)
        )
