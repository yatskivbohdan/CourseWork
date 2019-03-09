import hidden
import http.client
import json

#Creating connection 
connection = http.client.HTTPConnection('api.football-data.org')
headers = {'X-Auth-Token': hidden.token, 'X-Response-Control': 'minified'}
#Making request
connection.request('GET', '/v2/competitions/PL/scorers', None, headers)
#Loading request into json file
scorers = json.loads(connection.getresponse().read().decode())
for player in scorers['scorers']:
    print(player['player']['name'] + " "*(26-len(player['player']['name'])) +
          player['team']['name'] + " "*(26-len(player['team']['name'])) +
          str(player['numberOfGoals']))
connection.request('GET', '/v2/competitions/PL/matches', None, headers)
matches = json.loads(connection.getresponse().read().decode())
with open("results.json", 'w', encoding = 'utf-8') as results:
    for match in matches['matches']:
        json.dump(match, results)
