from fixtures.fixture import Fixture, Team, Probabilities
from fixtures.fixture_provider import FixtureProvider


def test_upcoming_fixtures():
    fake_requests = FakeFixtureRequests()
    provider = FixtureProvider("some-api-key", fake_requests)

    fixtures = provider.upcoming_fixtures()

    assert fake_requests.request_url == "https://api.the-odds-api.com/v3/odds" \
                                        "?sport=soccer_epl&region=us&mkt=h2h&apiKey=some-api-key"
    assert fixtures == [
        Fixture(Team("Chelsea"), Team("Swansea"), Probabilities(0.129154652, 0.658863257, 0.211982091), 1544967000),
        Fixture(Team("Colorado Rapids"), Team("Bournemouth"), Probabilities(0.5, 0.25, 0.25), 1544967000),
    ]


class FakeFixtureRequests(object):
    def __init__(self):
        self.request_url: str = None

    def get(self, url: str):
        self.request_url = url
        return FakeResponse()


class FakeResponse(object):
    def __init__(self):
        self.text = """
{
  "success": true,
  "data": [
    {
      "sport_key": "soccer_epl",
      "sport_nice": "EPL",
      "teams": [
        "Swansea",
        "Chelsea"
      ],
      "commence_time": 1544967000,
      "home_team": "Chelsea",
      "sites": [
        {
          "site_key": "betfair",
          "site_nice": "Betfair",
          "last_update": 1544919947,
          "odds": {
            "h2h": [
              7.55,
              1.48,
              4.6
            ]
          }
        },
        {
          "site_key": "ladbrokes",
          "site_nice": "Ladbrokes",
          "last_update": 1544919959,
          "odds": {
            "h2h": [
              7,
              1.44,
              4.2
            ]
          }
        }
      ],
      "sites_count": 12
    },
    {
      "sport_key": "soccer_epl",
      "sport_nice": "EPL",
      "teams": [
        "Colorado Rapids",
        "Bournemouth"
      ],
      "commence_time": 1544967000,
      "home_team": "Colorado Rapids",
      "sites": [
        {
          "site_key": "betfair",
          "site_nice": "Betfair",
          "last_update": 1544919947,
          "odds": {
            "h2h": [
              1.95,
              3.9,
              3.9
            ]
          }
        },
        {
          "site_key": "ladbrokes",
          "site_nice": "Ladbrokes",
          "last_update": 1544919959,
          "odds": {
            "h2h": [
              1.87,
              3.8,
              3.7
            ]
          }
        }
      ],
      "sites_count": 12
    }
  ]
}
        """
