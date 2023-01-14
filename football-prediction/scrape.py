import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

#returns list of two teams arranged [home, away]
def team_names(link):
    req = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
    soup = bs(req.content, "html.parser")
    home = soup.find("div", class_='sb-team sb-heim')
    away = soup.find("div", class_='sb-team sb-gast')
    try:
        return [home.find_all('a')[-1].text, away.find_all('a')[-1].text]
    except AttributeError:
        print(soup.find_all('div'))
        return ['', '']

df = pd.read_excel('games.xls','games')
df = df.loc[df['competition_code'] == 'GB1']
df = df.reset_index()
home_l = []
away_l = []

for i in range(len(df.index)):
    url = df['url'][i]
    teams = team_names(url)
    if teams == ['', '']:
        print(url)
        break
    home_l.append(teams[0])
    away_l.append(teams[1])

print(home_l)
print(away_l)

df['home_team'] = home_l
df['away_team'] = away_l

df.to_csv('games_updated.csv')
