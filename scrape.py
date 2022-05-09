from random import betavariate
from bs4 import BeautifulSoup
import requests

url = 'https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures'

req_data = {
            "Total Goals For" : 0,
            "Total Goals Against" : 0,
            "Goals Scored Against Opponent" : 0,
            "Goals Conceded Against Opponent" : 0
           }

def find_team_page(team_name):
    data = requests.get(url)
    raw = BeautifulSoup(data.text, 'html.parser')
    body = raw.find(lambda tag: tag.name == 'tbody')
    rows = body.find_all('tr')
    my_lst = []

    for i in rows:
        col = i.find(lambda tag: tag.name == "td" and tag.has_attr('data-stat') and tag['data-stat'] == 'squad_a')
        my_lst.append(col)

    for i in my_lst:
        a = i.find(lambda tag: tag.name == "a" and team_name in tag["href"])
        if a:
            new_url = a["href"]
            break
    
    return new_url

def add_team_goals_for(team_name):
    team_url = "https://fbref.com" + find_team_page(team_name)
    team_data = requests.get(team_url)
    raw = BeautifulSoup(team_data.text, 'html.parser')
    footer = raw.find(lambda tag: tag.name == "tfoot")
    req_row = footer.find('tr')

    goal_row = req_row.find(lambda tag: tag.name == 'td' and tag["data-stat"] == "goals")
    req_data["Total Goals For"] = int(goal_row.text)

def add_team_goals_against(team_name):
    team_url = "https://fbref.com" + find_team_page(team_name)
    team_data = requests.get(team_url)
    raw = BeautifulSoup(team_data.text, 'html.parser')
    footer = raw.find(lambda tag: tag.name == "tfoot")
    rows = footer.find_all('tr')
    req_row = rows[1]

    goal_row = req_row.find(lambda tag: tag.name == 'td' and tag["data-stat"] == "goals")
    req_data["Total Goals Against"] = int(goal_row.text)


