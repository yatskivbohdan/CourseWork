import json
from ADT.adt import MatchList


class League:
    """Represents a league class"""
    def __init__(self, code):
        self.code = code
        self._standings = self.__get_standings()
        self.matches = self.__get_matches()
        self.teams = self.__get_teams()

    def __get_teams(self):
        """
        Returns a dict
        key = team name
        item = Team object
        :return: dict
        """
        teams = {}
        with open("data/" + self.code + "teams.json", "r", encoding="utf-8") as file:
            teams_js = json.load(file)
        self.matchday = teams_js['season']['currentMatchday'] - 1
        for team in teams_js['teams']:
            teams[team['name']] = Team(team['name'], team['id'], self.matches, self.matchday, self._standings)
        return teams

    def __get_standings(self):
        """
        Returns a dictionary where key is team name and value is the team`s position
        :return: dict
        """
        standings = {}
        with open("data/" + self.code + "standings.json", "r", encoding="utf-8") as file:
            standings_js = json.load(file)
        for team in standings_js['standings'][0]['table']:
            standings[team['team']['name']] = team['position']
        return standings

    def print_standings(self):
        """
        Prints the standings
        :return: None
        """
        with open("data/" + self.code + "standings.json", "r", encoding="utf-8") as file:
            standings_js = json.load(file)
        print("Premier League")
        print("№ " + "Name" + (24*" ") + "G  W  D  L  GF  GA  GD   P")
        for team in standings_js['standings'][0]['table']:
            print((2-len(str(team['position'])))*" " + str(team['position']) + " " + team['team']['name'] +
                  (27 - len(team['team']['name']))*" " + " "*(2-len(str(team['playedGames']))) +
                  str(team['playedGames']) + " " * (3 - len(str(team['won']))) + str(team['won']) +
                  " " * (3 - len(str(team['draw']))) + str(team['draw']) +
                  " " * (3 - len(str(team['lost']))) + str(team['lost']) + " " * (4 - len(str(team['goalsFor']))) +
                  str(team['goalsFor']) + " " * (4 - len(str(team['goalsAgainst']))) + str(team['goalsAgainst']) +
                  " " * (4 - len(str(team['goalDifference']))) + str(team['goalDifference']) +
                  (" " * (4 - len(str(team['points']))) + str(team['points'])))

    def print_scorers(self):
        """
        Prints a list of top 10 scorers of the league
        :return: None
        """
        with open("data/" + self.code + "scorers.json", "r", encoding="utf-8") as file:
            scorers = json.load(file)
        print("Top Scorers:")
        num = 1
        for player in scorers['scorers']:
            print(" "*(2 - len(str(num))) + str(num) + "." + player['player']['name'] +
                  " "*(26-len(player['player']['name'])) +
                  player['team']['name'] + " "*(26-len(player['team']['name'])) +
                  str(player['numberOfGoals']))
            num += 1

    def __get_matches(self):
        """
        Returns all league matches
        :return: MatchList object
        """
        with open("data/" + self.code + "matches.json", "r", encoding="utf-8") as file:
            matches_js = json.load(file)
        lst = matches_js['matches']
        matches = MatchList()
        for match in lst:
            matches.append((match['status'], match['matchday'], match['homeTeam']['name'],
                            match['awayTeam']['name'], match['score']['fullTime']))
        return matches

    def print_matchday(self, num):
        """
        Prints all matches of given matchday
        :param num: matchday number
        :return: None
        """
        matches = ""
        for match in self.matches.get_matchday(num):
            matches += "{} {}-{} {}".format(match[2], match[4]['homeTeam'], match[4]['awayTeam'], match[3]) + "\n"
        print("MatchDay {}".format(num))
        print(matches)


class Team:
    """Represents one football team"""
    def __init__(self, name, team_id, match_list, matchday, standings):
        self.name = name
        self.id = team_id
        self.match_list = match_list
        self._matchday = matchday
        self.position = standings[self.name]
        self._standings = standings
        self._all_matches = None
        self._stat = None
        self._stat_percentage = None
        self._games_num = None
        self._goals = None
        self._home_matches = None
        self._away_matches = None
        self._home_stat = None
        self._away_stat = None
        self._home_stat_percentage = None
        self._away_stat_percentage = None
        self._home_goals = None
        self._away_goals = None
        self._avg_goals_scored = None
        self._avg_goals_missed = None
        self._home_goals_avg_scored = None
        self._home_goals_avg_missed = None
        self._away_goals_avg_scored = None
        self._away_goals_avg_missed = None
        self._top6_stat = None
        self.get_stats()
        self._form = self.get_form(5)

    def get_stats(self):
        """
        Finds the stats and gives the values to the atributes
        :return: None
        """
        self._all_matches = self.match_list.get_team_matches(self.name)
        self._stat = self.match_list.get_stats(self.name)
        self._stat_percentage = (round((self._stat[1]/self._stat[0])*100, 1),
                                 round((self._stat[2]/self._stat[0])*100, 1),
                                 round((self._stat[3]/self._stat[0])*100, 1))
        self._games_num = self._stat[0]
        self._goals = self.match_list.get_goals(self.name)
        self._home_matches = self.match_list.get_home_matches(self.name)
        self._away_matches = self.match_list.get_away_matches(self.name)
        self._home_stat = self._home_matches.get_stats(self.name)
        self._away_stat = self._away_matches.get_stats(self.name)
        self._home_stat_percentage = (round((self._home_stat[1] / self._home_stat[0])*100, 1),
                                round((self._home_stat[2] / self._home_stat[0])*100, 1),
                                round((self._home_stat[3] / self._home_stat[0])*100, 1))
        self._away_stat_percentage = (round((self._away_stat[1] / self._away_stat[0])*100, 1),
                                round((self._away_stat[2] / self._away_stat[0])*100, 1),
                                round((self._away_stat[3] / self._away_stat[0])*100, 1))

        self._home_goals = self._home_matches.get_goals(self.name)
        self._away_goals = self._away_matches.get_goals(self.name)
        self._avg_goals_scored = round(self._goals[0] / self._games_num, 2)
        self._avg_goals_missed = round(self._goals[1] / self._games_num, 2)
        self._home_goals_avg_scored = round(self._home_goals[0] / (self._home_stat[0]), 2)
        self._home_goals_avg_missed = round(self._home_goals[1] / (self._home_stat[0]), 2)
        self._away_goals_avg_scored = round(self._away_goals[0] / (self._away_stat[0]), 2)
        self._away_goals_avg_missed = round(self._away_goals[1] / (self._away_stat[0]), 2)
        self._top6_stat = self.against_top_6()

    def get_form(self, num):
        """
        Returns a MatchList class object that contains last number(num) of matches
        :param num: number of last matches
        :return: MatchList object
        """
        return self._all_matches[self._matchday-num:self._matchday]

    def against_top_6(self):
        """
        Returns a MatchList class object with matches only against top 6 teams in league
        :return: MatchList object
        """
        against_top6 = MatchList()
        for match in self._all_matches:
            if (self._standings[match[2]] <= 6 and match[2] != self.name) or \
                    (self._standings[match[3]] <= 6 and match[3] != self.name):
                against_top6.append(match)
        return against_top6.get_stats(self.name)

    def print_info(self):
        print('''
Team name: {}
Position: {}
OVERALL statistics:
Wins - {}({}%) Draws - {}({}%) Loses - {}({}%)
Goals scored - {}
Goals missed - {}
Goals per game scored(average) - {}
Goals per game missed(average) - {}
Statistics against top 6 teams:
Wins - {} Draws - {} Loses - {}
---------------------------------------------
HOME statistics:
Wins - {}({}%) Draws - {}({}%) Loses - {}({}%)
Goals scored - {}
Goals missed - {}
Goals per game scored(average) - {}
Goals per game missed(average) - {}
---------------------------------------------
AWAY statistics:
Wins - {}({}%) Draws - {}({}%) Loses - {}({}%)
Goals scored - {}
Goals missed - {}
Goals per game scored(average) - {}
Goals per game missed(average) - {}
---------------------------------------------
FORM(Last 5 games):
{} {}-{} {}
{} {}-{} {}
{} {}-{} {}
{} {}-{} {}
{} {}-{} {}
'''.format(self.name, self.position, self._stat[1], self._stat_percentage[0], self._stat[2], self._stat_percentage[1],
           self._stat[3], self._stat_percentage[2], self._goals[0], self._goals[1], self._avg_goals_scored,
           self._avg_goals_missed, self._top6_stat[1], self._top6_stat[2], self._top6_stat[3],
           self._home_stat[1], self._home_stat_percentage[0], self._home_stat[2], self._home_stat_percentage[1],
           self._home_stat[3], self._home_stat_percentage[2], self._home_goals[0], self._home_goals[1],
           self._home_goals_avg_scored, self._home_goals_avg_missed,
           self._away_stat[1], self._away_stat_percentage[0], self._away_stat[2], self._away_stat_percentage[1],
           self._away_stat[3], self._away_stat_percentage[2], self._away_goals[0], self._away_goals[1],
           self._away_goals_avg_scored, self._away_goals_avg_missed,
           self._form[0][2], self._form[0][4]['homeTeam'], self._form[0][4]['awayTeam'], self._form[0][3],
           self._form[1][2], self._form[1][4]['homeTeam'], self._form[1][4]['awayTeam'], self._form[1][3],
           self._form[2][2], self._form[2][4]['homeTeam'], self._form[2][4]['awayTeam'], self._form[2][3],
           self._form[3][2], self._form[3][4]['homeTeam'], self._form[3][4]['awayTeam'], self._form[3][3],
           self._form[4][2], self._form[4][4]['homeTeam'], self._form[4][4]['awayTeam'] , self._form[4][3]))

    def print_head_to_head(self, other_team):
        """
        Prints comparison of two teams and their previous games against each other
        :param other_team:
        :return:
        """
        head_to_head_matches = self._all_matches.get_team_matches(other_team.name)
        matches = ""
        for match in head_to_head_matches:
            matches += "{} {}-{} {}".format(match[2], match[4]['homeTeam'], match[4]['awayTeam'], match[3]) + "\n"
        self.print_info()
        other_team.print_info()
        print("Previous matches:\n" + matches)
