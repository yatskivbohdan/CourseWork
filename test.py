import hidden
import http.client
import json


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
