import requests
from bs4 import BeautifulSoup

class tables:
    data = None
    raw = None

    def __init__(self, url):
        self.data = requests.get(url)
        self.raw = BeautifulSoup(self.data.text, 'html.parser')

    def home_goals(self, team_name):
        div = self.raw.find(lambda tag: tag.name == 'div' and tag.has_attr('id') and tag['id'] == 'h2h-team1')
        table = div.find('table')
        rows = table.find_all('tr')
        
        for row in rows:
            col = row.find(lambda tag: tag.name == 'td' and tag.has_attr('style'))
            if col:
                if team_name in col.text:
                    req = row.find(lambda tag: tag.name == 'font' and tag['color'] == 'blue')
                    if req:
                        return int(req.text)
    
    def away_goals(self, team_name):
        div = self.raw.find(lambda tag: tag.name == 'div' and tag.has_attr('id') and tag['id'] == 'h2h-team2')
        table = div.find('table')
        rows = table.find_all('tr')
        
        for row in rows:
            col = row.find(lambda tag: tag.name == 'td' and tag.has_attr('style'))
            if col:
                if team_name in col.text:
                    req = row.find(lambda tag: tag.name == 'font' and tag['color'] == 'blue')
                    if req:
                        return int(req.text)
