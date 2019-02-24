import hidden
import http.client
import json


#"f197b7b02f4244c4b7080c704dbf4a25": FOOTBALL_DATA_API
connection = http.client.HTTPConnection('api.football-data.org')
headers = {'X-Auth-Token': hidden.token, 'X-Response-Control': 'minified'}
connection.request('GET', '/v2/competitions/PL/scorers', None, headers)
scorers = json.loads(connection.getresponse().read().decode())
for player in scorers['scorers']:
    print(player['player']['name'] + " "*(26-len(player['player']['name'])) +
          player['team']['name'] + " "*(26-len(player['team']['name'])) +
          str(player['numberOfGoals']))
connection.request('GET', '/v2/competitions/PL/matches', None, headers)
matches = json.loads(connection.getresponse().read().decode())
with open("F:/Programming/Labs/CourseWork/results.json", 'w', encoding = 'utf-8') as results:
    for match in matches['matches']:
        json.dump(match, results)



#print(data.get_available_competitions())
#data.competition = "premier league"
#teams_in_premier = data.get_info('teams')
#print(data.get_info('matches'))
#from datetime import datetime
#date_today = datetime.today()
#matches = data.get_info('matches', dateFrom='2018-08-01', dateTo=date_today)
#for i in matches["filters"]:
#    print(i)
