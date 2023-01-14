import pandas as pd
import data

df = pd.read_csv("games_updated.csv")

def new_home_away_avg(cur_season, home, away):
    last_5 = [cur_season - 1, cur_season - 2, cur_season - 3, cur_season - 4, cur_season - 5]
    overall = [0, 0, 0, 0]
    home_team = [0, 0, 0, 0]
    away_team = [0, 0, 0, 0]
    for i in last_5:
        tup = data.home_away_avg(i, home, away)
        for i in range(len(overall)):
            overall[i] += tup[0][i]
            home_team[i] += tup[1][i]
            away_team[i] += tup[2][i]
    overall[1], overall[3] = overall[1]/5, overall[3]/5
    home_team[2], home_team[3] = home_team[2]/5, home_team[3]/5
    away_team[2], away_team[3] = away_team[2]/5, away_team[3]/5

    return (overall, home_team, away_team)

