from tkinter import *
from tkinter import ttk
from classes import League


# Defining global variables
curr_league = None
curr_team = None
curr_matchday = None
scorers = None
stat = None
combo_t = None
combo_c = None
choose_bt = None
choose_bm = None
compare_bt = None
combo_m = None
compare_option = None
match_option = None
team_option = None
comparison = None
compare_label = None


def league_update():
    global scorers
    global combo_t
    global stat
    global choose_bt
    global choose_bm
    global combo_m
    global combo_c
    global compare_option
    global curr_matchday
    global compare_bt
    global comparison
    global compare_label
    if scorers:
        scorers.destroy()
    if combo_t:
        combo_t.destroy()
    if combo_m:
        combo_m.destroy()
    if stat:
        stat.destroy()
    if choose_bt:
        choose_bt.destroy()
    if choose_bm:
        choose_bm.destroy()
    if curr_matchday:
        curr_matchday.destroy()
    if combo_c:
        combo_c.destroy()
    if compare_option:
        compare_option.destroy()
    if compare_bt:
        compare_bt.destroy()
    if comparison:
        comparison.destroy()
    if compare_label:
        compare_label.destroy()
    root.update()


def league_menu():
    global curr_league
    global curr_team
    global matchday_option
    global team_option
    league_update()
    curr_league = League(leagues[league.get()])
    Label(root, text=curr_league.print_standings(), width=60, height=23, justify=LEFT, font="Consolas 12").place(x=50,
                                                                                                                 y=100)
    Button(root, text='Get scorers', command=print_scorers).place(x=25, y=550)
    matchday_option = Button(root, text='Get matchday', command=matchday)
    matchday_option.place(x=25, y=585)
    team_option = Button(root, text='Choose team', command=team_menu)
    team_option.place(x=225, y=550)



def print_scorers():
    global scorers
    if scorers:
        scorers.destroy()
    scorers = Label(root, text=curr_league.print_scorers(), width=60, height=30, anchor=NW, font="Consolas 12")
    scorers.place(x=650, y=100)


def team_menu():
    global combo_t
    global choose_bt
    global team_option
    team_option.destroy()
    Label(root, text='Choose team').place(x=225, y=550)
    combo_t = ttk.Combobox(root, width=15, textvariable=team)
    combo_t['values'] = tuple(curr_league.teams.keys())
    combo_t.place(x=325, y=550)
    choose_bt = Button(root, text='Choose', command=team_stat)
    choose_bt.place(x=325, y=575)


def team_stat():
    global stat
    global curr_team
    global compare_option
    curr_team = curr_league.teams[team.get()]
    if stat:
        stat.destroy()
    stat = Label(root, text=curr_team.print_info(), width=68, height=35, anchor=NW, font="Consolas 11")
    stat.place(x=650, y=100)
    compare_option = Button(root, text='Compare with another team', command=compare)
    compare_option.place(x=450, y=550)


def matchday():
    global combo_m
    global choose_bm
    global matchday_option
    matchday_option.destroy()
    Label(root, text='Get matchday').place(x=25, y=585)
    combo_m = ttk.Combobox(root, width=15, textvariable=md_num)
    if curr_league.code == "BL1":
        combo_m['values'] = [i for i in range(1, 35)]
    else:
        combo_m['values'] = [i for i in range(1, 39)]
    combo_m.place(x=125, y=585)
    choose_bm = Button(root, text='Choose', command=print_matchday)
    choose_bm.place(x=125, y=610)

def print_matchday():
    global curr_matchday
    if curr_matchday:
        curr_matchday.destroy()
    curr_matchday = Label(root, text=curr_league.print_matchday(int(md_num.get())), width=60, height=30, anchor=NW,
                    font="Consolas 12")
    curr_matchday.place(x=650, y=100)

def compare():
    global compare_option
    global compare_bt
    global combo_c
    global compare_label
    compare_option.destroy()
    compare_label = Label(root, text='Compare with another team')
    compare_label.place(x=450, y=550)
    combo_c = ttk.Combobox(root, width=15, textvariable=compared_team)
    combo_c['values'] = tuple(curr_league.teams.keys())
    combo_c.place(x=450, y=575)
    compare_bt = Button(root, text='Choose', command=print_comparison)
    compare_bt.place(x=450, y=600)

def print_comparison():
    global comparison
    if comparison:
        comparison.destroy()
    comparison_team = curr_league.teams[compared_team.get()]
    comparison = Label(root, text=curr_team.print_head_to_head(comparison_team),  width=75, height=40,  anchor=W,
                    font="Consolas 10")
    comparison.place(x=650, y=100)


root = Tk()
root.title('FootballDataAnalysis')
root.iconbitmap('football.ico')
root.geometry('1455x825')

leagues = {"Premier League(ENG)": "PL", "La Liga(ESP)": "PD", "Bundesliga(GER)": "BL1", "Serie A(ITA)": "SA",
               "Ligue 1(FRA)": "FL1"}


background_image = PhotoImage(file='background.gif')
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.update()


Label(root, text='Choose a league:').place(x=25, y=10)

league = StringVar()
team = StringVar()
md_num = StringVar()
compared_team = StringVar()


combo = ttk.Combobox(root, width=15, textvariable = league)
combo['values'] = ('Premier League(ENG)', 'La Liga(ESP)', 'Bundesliga(GER)', 'Serie A(ITA)', 'Ligue 1(FRA)')
combo.place(x=25, y=40)

choose_league = Button(root, text='Choose', command=league_menu).place(x=25, y=70)


root.mainloop()
