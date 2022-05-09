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
