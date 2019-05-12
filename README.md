# Football Data Analysis Project
Project by Bohdan Yatskiv for my coursework at UCU.

Application allows to get statistics for each team from following leagues:

 - Premier League(ENG)
 - La Liga(ESP)
 - Bundesliga(GER)
 - Serie A(ITA)
 - Ligue 1(FRA)

## Description
This program allows you to get detailed statistics like average goals per game, home and away statistics, wins percentage
for any team from top 5 leagues and compare it with other teams. 

## Input and output
The program input is name of the league and team name.
The output is statistics data.

## Modules description
* main.py - main module that runs the program
   - class Menu - helps to control the program by user input comands
* classes.py - module that contains data structure classes
   - class League 
   - class Team
* adt.py - module with ADT
   - class MatchList
      - choose_league
      - get_standings
      - get_scorers
      - get_matchday
      - choose_team
      - get_stats
      - compare
   
* updater.py = module that updates .json files with all necessary data   
