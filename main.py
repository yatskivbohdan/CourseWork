from classes import League, Team


class Menu():
    def __init__(self):
        self.menu_map = {
            "choose another league": self.choose_league,
            "get standings": self.get_standings,
            "get scorers": self.get_scorers,
            "get matchday": self.get_matchday,
            "choose a team": self.choose_team,
            "quit": self.quit
        }
        self._league = None

    def choose_league(self):
        print("\nEnter the league:\nPremier League(ENG)\nLa Liga(ESP)\nBundesliga(GER)\nSerie A(ITA)\nLigue 1(FRA)")
        leagues = {"Premier League":"PL", "La Liga": "PD", "Bundesliga": "BL1", "Serie A": "SA", "Ligue 1": "FL1"}
        league = input("enter league name:")
        try:
            league_id = leagues[league]
            self._league = League(league_id)
            print("You have successfully chosen the league")
        except KeyError:
            print("Enter a valid league name!")
            self.choose_league()

    def get_standings(self):
        self._league.print_standings()

    def get_scorers(self):
        self._league.print_scorers()

    def get_matchday(self):
        valid = False
        while not valid:
            num = int(input("Enter the matchday number:"))
            if self._league.code == "BL1":
                if num >= 1 and num <= 34:
                    valid = True
                else:
                    print("Enter a valid matchday number!")
            else:
                if num >= 1 and num <= 38:
                    valid = True
                else:
                    print("Enter a valid matchday number!")
        self._league.print_matchday(num)

    def choose_team(self):
        self._league.print_standings()
        valid = False
        while not valid:
            answer = input("Enter the team name:")
            if answer in self._league.teams:
                team = self._league.teams[answer]
                valid = True
            else:
                print("Enter valid team name!")
        self.team_menu(team)

    def team_menu(self, team):
        team_menu_map = {
            "get stats": self.get_stats,
            "compare": self.compare,
            "back": self.menu
        }
        while True:
            print("""
Please enter a command:

\tget stats---Get detailed team statistics
\tcompare---Compare two teams head to head
\tback---Go back to previous page
""")
            answer = input("Enter a command:")
            try:
                func = team_menu_map[answer]
            except KeyError:
                print("{} is not a valid command".format(answer))
            else:
                if answer != "back":
                    func(team)
                else:
                    func()



    def get_stats(self, team):
        team.print_info()

    def compare(self, team):
        valid = False
        while not valid:
            answer = input("Enter the name of team you want compare with:")
            if answer in self._league.teams:
                another_team = self._league.teams[answer]
                valid = True
            else:
                print("Enter valid team name!")
        team.print_head_to_head(another_team)

    def quit(self):
        print("Thank you for using our program!")
        raise SystemExit

    def menu(self):
        if not self._league:
            print("Welcome to the Football Data Analysis app")
            print("Please choose a league:")
            self.choose_league()
        try:
            while True:
                print("\n")
                print("""
Please enter a command:

\tget standings ---Get league standings
\tget scorers---Get list of league top scorers
\tget matchday---Get all matches of the chosen matchday
\tchoose a team---Choose a team and get it stats
\tchoose another league---Choose another league
\tquit---Quit the program
""")
                answer = input("Enter a command: ").lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print("{} is not a valid command".format(answer))
                else:
                    func()
           
        
menu = Menu()
menu.menu()



