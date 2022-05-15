import scrape_all_teams as all
from bs4 import BeautifulSoup
import requests

url = 'https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures'
url2 = 'https://www.soccerstats.com/homeaway.asp?league=england'

req_data = {
            "Total Goals For" : 0,
            "Total Goals Against" : 0,
            "Total Home Goals Scored" : 0,
            "Total Away Goals Scored" : 0,
            "Opponent Total Goals For" : 0,
            "Opponent Total Goals Against" : 0,
            "Opponent Total Home Goals Scored" : 0,
            "Opponent Total Away Goals Scored" : 0,
            "Goals Scored Against Opponent" : 0,
            "Goals Conceded Against Opponent" : 0,
            "Total Home Goals Scored By All Teams" : 0,
            "Total Away Goals Scored By All Teams" : 0,
           }

tables = all.tables(url2)


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

def add_team_goals_for(team_name, isOpponent):
    team_url = "https://fbref.com" + find_team_page(team_name)
    team_data = requests.get(team_url)
    raw = BeautifulSoup(team_data.text, 'html.parser')
    footer = raw.find(lambda tag: tag.name == "tfoot")
    req_row = footer.find('tr')

    goal_row = req_row.find(lambda tag: tag.name == 'td' and tag["data-stat"] == "goals")

    if isOpponent:
        req_data["Opponent Total Goals For"] = int(goal_row.text)
    else:    
        req_data["Total Goals For"] = int(goal_row.text)

def add_team_goals_against(team_name, isOpponent):
    team_url = "https://fbref.com" + find_team_page(team_name)
    team_data = requests.get(team_url)
    raw = BeautifulSoup(team_data.text, 'html.parser')
    footer = raw.find(lambda tag: tag.name == "tfoot")
    rows = footer.find_all('tr')
    req_row = rows[1]

    goal_row = req_row.find(lambda tag: tag.name == 'td' and tag["data-stat"] == "goals")

    if isOpponent:
        req_data["Opponent Total Goals Against"] = int(goal_row.text)
    else:
        req_data["Total Goals Against"] = int(goal_row.text)

def add_goals_against_opponent(team_name, opponent_name):
    team_url = "https://fbref.com" + find_team_page(team_name)
    team_data = requests.get(team_url)
    raw = BeautifulSoup(team_data.text, 'html.parser')
    div = raw.find(lambda tag: tag.name == "div" and tag.has_attr("id") and tag["id"] == "all_matchlogs")
    body = div.find("tbody")

    rows = body.find_all("tr")
    goals = 0

    for row in rows:
        opponent_data = row.find(lambda tag: tag.name == "td" and tag["data-stat"] == "opponent")
        if opponent_data.text == opponent_name:
            scored = row.find(lambda tag: tag.name == "td" and tag["data-stat"] == "goals_for").text
            goals += int(scored)

    req_data["Goals Scored Against Opponent"] = goals

def add_goals_conceded_against_opponent(team_name, opponent_name):
    team_url = "https://fbref.com" + find_team_page(team_name)
    team_data = requests.get(team_url)
    raw = BeautifulSoup(team_data.text, 'html.parser')
    div = raw.find(lambda tag: tag.name == "div" and tag.has_attr("id") and tag["id"] == "all_matchlogs")
    body = div.find("tbody")

    rows = body.find_all("tr")
    goals = 0

    for row in rows:
        opponent_data = row.find(lambda tag: tag.name == "td" and tag["data-stat"] == "opponent")
        if opponent_data.text == opponent_name:
            conceded = row.find(lambda tag: tag.name == "td" and tag["data-stat"] == "goals_against").text
            goals += int(conceded)

    req_data["Goals Conceded Against Opponent"] = goals

def add_home_goals_scored(team_name, isOpponent):
    goals = tables.home_goals(team_name)
    
    if isOpponent:
        req_data["Opponent Total Home Goals Scored"] = goals
    else:
        req_data["Total Home Goals Scored"] = goals

def add_away_goals_scored(team_name, isOpponent):
    goals = tables.away_goals(team_name)
    
    if isOpponent:
        req_data["Opponent Total Home Goals Scored"] = goals
    else:
        req_data["Total Home Goals Scored"] = goals
