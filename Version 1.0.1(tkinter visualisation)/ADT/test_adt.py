from adt import MatchList
from unittest import TestCase, main
import results
import json


class TestMatchList(TestCase):
    def setUp(self):
        with open("PLmatches.json", 'r') as file:
            matches_js = json.load(file)
        lst = matches_js['matches']
        self.matches = MatchList()
        for match in lst:
            self.matches.append((match['status'], match['matchday'], match['homeTeam']['name'],
                            match['awayTeam']['name'], match['score']['fullTime']))

    def test_get_matchday(self):
        matchday3 = self.matches.get_matchday(3)
        matchday35 = self.matches.get_matchday(35)
        matchday40 = self.matches.get_matchday(40)
        self.assertEqual(matchday3, results.matchday_3)
        self.assertEqual(matchday35, results.matchday_35)
        self.assertEqual(matchday40, results.matchday_40)

    def test_get_team_matches(self):
        liverpool = self.matches.get_team_matches("Liverpool FC")
        barcelona = self.matches.get_team_matches("Barcelona FC")
        self.assertEqual(liverpool, results.liverpool)
        self.assertEqual(barcelona, results.barcelona)

    def test_get_home_matches(self):
        liverpool_home = self.matches.get_home_matches("Liverpool FC")
        self.assertEqual(liverpool_home, results.liverpool_home)

    def test_get_away_matches(self):
        liverpool_away = self.matches.get_away_matches("Liverpool FC")
        self.assertEqual(liverpool_away, results.liverpool_away)

    def test_get_stats(self):
        liverpool_stat = self.matches.get_stats("Liverpool FC")
        mancity_stat = self.matches.get_stats("Manchester City FC")
        barcelona_stat = self.matches.get_stats("Barcelona FC")
        self.assertEqual(liverpool_stat, results.liverpool_stat)
        self.assertEqual(mancity_stat, results.mancity_stat)
        self.assertEqual(barcelona_stat, results.barcelona_stat)

    def test_get_goals(self):
        liverpool_goals = self.matches.get_goals("Liverpool FC")
        barcelona_goals = self.matches.get_goals("Barcelona FC")
        self.assertEqual(liverpool_goals, results.liverpool_goals)
        self.assertEqual(barcelona_goals, results.barcelona_goals)

if __name__ == "__main__":
    unittest.main()


