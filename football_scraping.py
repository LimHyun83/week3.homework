import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://sports.news.naver.com/kfootball/record/index.nhn?category=kleague&year=2020',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

teams = soup.select('#regularGroup_table > tr')

for team in teams:
    image_team = team.select_one('td.tm > div > img')
    team_name = team.select_one('td.tm > div > span').text
    team_record = team.select_one('th > strong').text
    team_score = team.select_one('td > strong').text


    if image_team:
        print(team_record, team_name, team_score)


