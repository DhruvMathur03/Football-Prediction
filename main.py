import math
import data
import cur_season
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv("games_updated.csv")

home_team = str(input("Enter Home Team Name : "))
away_team = str(input("Enter Away Team Name : "))
season = int(input("Enter Season : "))

new_flag = True

for i in range(len(df['home_team'])):
    if home_team in df['home_team'][i]:
        home_team = df['home_team'][i]
    if away_team in df['away_team'][i]:
        away_team = df['away_team'][i]
    if season == df['season'][i]:
        new_flag = False


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
home_goals_prob = np.array([poisson_probability(exp_home_goals, i) for i in range(6)])
home_goals_probs = np.round(home_goals_prob,2)

X = [0,1,2,3,4,5]

fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.plot(X, home_goals_probs, 'bo', ms=8)
plt.ylabel("Probability", fontsize="16")
plt.xlabel("No. of Goals", fontsize="16")
plt.title(home_team, fontsize="18")
ax.vlines(X, 0, home_goals_probs, colors='b', lw=5, alpha=0.5)
for i, v in enumerate(home_goals_probs):
    ax.text(i, v, str(v), color='red', fontweight='bold')

plt.show()

# Compute the Poisson probabilities for the range of possible goals scored by the away team
away_goals_prob = np.array([poisson_probability(exp_away_goals, i) for i in range(6)])
away_goals_probs = np.round(away_goals_prob,2)

fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.plot(X, away_goals_probs, 'bo', ms=8)
plt.ylabel("Probability", fontsize="16")
plt.xlabel("No. of Goals", fontsize="16")
plt.title(away_team, fontsize="18")
ax.vlines(X, 0, away_goals_probs, colors='b', lw=5, alpha=0.5)
for i, v in enumerate(away_goals_probs):
    ax.text(i, v, str(v), color='red', fontweight='bold')

plt.show()

def predicted_scoreline(home_exp, away_exp):
    home_exp = list(home_exp)
    away_exp = list(away_exp)
    max_home_prob = max(home_exp)
    max_away_prob = max(away_exp)
    home_goals = home_exp.index(max_home_prob)
    away_goals = away_exp.index(max_away_prob)
    print(home_goals, " - ", away_goals)

predicted_scoreline(home_goals_prob, away_goals_probs)


