from flask import Flask, request, jsonify
import math
import data
import cur_season
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/prediction', methods=['GET'])
def prediction():
    df = pd.read_csv("games_updated.csv")

    home_team = request.args.get('home_team')
    away_team = request.args.get('away_team')
    season = int(request.args.get('season'))

    new_flag = True

    for i in range(len(df['home_team'])):
        if home_team in df['home_team'][i]:
            home_team = df['home_team'][i]
        if away_team in df['away_team'][i]:
            away_team = df['away_team'][i]
        if season == df['season'][i]:
            new_flag = False

    #Compute the expected number of goals for the home and away teams
    def exp_goals(season, home, away):
        ret = []
        if new_flag:
            tup = cur_season.new_home_away_avg(season, home, away)
        else:
            tup = data.home_away_avg(season, home, away)
        home_attack_strength = tup[1][2]/tup[0][1]
        away_attack_strength = tup[2][2]/tup[0][3]

        home_def_strength = tup[1][3]/tup[0][3]
        away_def_strength = tup[2][3]/tup[0][1]

        home_exp_goal = home_attack_strength * away_def_strength * tup[0][1]
        ret.append(home_exp_goal)
        away_exp_goal = away_attack_strength * home_def_strength * tup[0][3]
        ret.append(away_exp_goal)

        return ret

    def poisson_probability(l, x):
        probability = ((l**x) * math.exp(-l)) / math.factorial(x)
        return probability*100

    # Compute the expected number of goals for the home and away teams
    exp_home_goals, exp_away_goals = exp_goals(season, home_team, away_team)

    # Compute the Poisson probabilities for the range of possible goals scored by the home team
    home_goals_prob = [poisson_probability(exp_home_goals, i) for i in range(6)]

    # Compute the Poisson probabilities for the range of possible goals scored by the away team
    away_goals_prob = [poisson_probability(exp_away_goals, i) for i in range(6)]

    response = jsonify({'home_goals_prob':home_goals_prob, 'away_goals_prob':away_goals_prob})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run()