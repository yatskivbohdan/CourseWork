import json
from adt import MatchList

with open("PLmatches.json", 'r') as file:
    matches_js = json.load(file)
lst = matches_js['matches']
matches = MatchList()
for match in lst:
    matches.append((match['status'], match['matchday'], match['homeTeam']['name'],
                      match['awayTeam']['name'], match['score']['fullTime']))

# matchday test
print(matches.get_matchday(35))
# home matches test
print(matches.get_home_matches("Liverpool FC"))

# matches between 2 teams test
liverpool = matches.get_team_matches("Liverpool FC")
livmc = liverpool.get_team_matches("Manchester City FC")
print(livmc)

# stats test
stats_liv = matches.get_stats("Liverpool FC")
print(stats_liv)

# home stats test
stats_liv_home = matches.get_home_matches("Liverpool FC").get_stats("Liverpool FC")
print(stats_liv_home)

# all goals or goals against other team test
liv_goals = matches.get_goals("Liverpool FC")
print(liv_goals)
print(livmc.get_goals("Liverpool FC"))
