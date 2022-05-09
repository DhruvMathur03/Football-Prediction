from bs4 import BeautifulSoup
import requests

url = 'https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures'
data = requests.get(url)

req_data = []
my_lst = []
raw = BeautifulSoup(data.text, 'html.parser')
body = raw.find(lambda tag: tag.name == 'tbody')

rows = body.find_all('tr')
for i in rows:
    col = i.find(lambda tag: tag.name == "td" and tag.has_attr('data-stat') and tag['data-stat'] == 'squad_a')
    my_lst.append(col)

for i in my_lst:
    a = i.find(lambda tag: tag.name == "a" and "Brentford" in tag["href"])
    print(a)
    break