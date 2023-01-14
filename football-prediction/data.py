import pandas as pd
import math

df = pd.read_csv("games_updated.csv")

#returns goals scored and conceded by team against opponent in a list [teams_goals, opponent_goals]

def home_away_avg(season, home, away):
    df_temp = df.loc[(df['season'] == season)]
    home_total = df_temp[['home_club_goals']].sum()
    home_avg = df_temp[['home_club_goals']].mean()
    away_total = df_temp[['away_club_goals']].sum()
    away_avg = df_temp[['away_club_goals']].mean()
    overall = [home_total[0], home_avg[0], away_total[0], away_avg[0]]

    df_temp = df.loc[(df['season'] == season) & (df['home_team'] == home)]
    home_goals_total = df_temp[['home_club_goals']].sum()
    home_goals_conceded = df_temp[['away_club_goals']].sum()
    home_team_avg = df_temp[['home_club_goals']].mean()
    home_team_conced_avg = df_temp[['away_club_goals']].mean()
    home_team = [home_goals_total[0], home_goals_conceded[0], home_team_avg[0], home_team_conced_avg[0]]

    df_temp = df.loc[(df['season'] == season) & (df['away_team'] == away)]
    away_goals_total = df_temp[['away_club_goals']].sum()
    away_goals_conceded = df_temp[['away_club_goals']].sum()
    away_team_avg = df_temp[['away_club_goals']].mean()
    away_team_conced_avg = df_temp[['away_club_goals']].mean()
    away_team = [away_goals_total[0], away_goals_conceded[0], away_team_avg[0], away_team_conced_avg[0]]
    return (overall, home_team, away_team)