import json
from typing import Dict, List

from soccerodds.fixtures.fixture import Fixture, Team, Odds


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
            odds=self.__calculate_odds(odds, home_team_index),
            start_time=fixture_dict["commence_time"]
        )

    @staticmethod
    def __calculate_odds(odds: List[float], home_team_index: int) -> Odds:
        return Odds(
            home=odds[home_team_index],
            draw=odds[2],
            away=odds[1 - home_team_index]
        )
