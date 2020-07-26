import requests
import lxml.etree

import pandas as pd
from bs4 import BeautifulSoup
import re

url = 'https://maoyan.com/films?showType=3'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
cookie = 'uuid_n_v=v1; uuid=D62230D0CF3611EABDA91DE1C2FF6305B6631D4EAD274DCA9B7099E9AD80DC61; _csrf=c9f32a7002f7ff953bd75a25e1c113b5e10545ca424e5a02f227eecbcf5ea6df; mojo-uuid=c0052bcd8b1aefe904a79e91bcab99b8; _lxsdk_cuid=1738af9f112c8-005435309de155-4353760-1fa400-1738af9f112c8; _lxsdk=D62230D0CF3611EABDA91DE1C2FF6305B6631D4EAD274DCA9B7099E9AD80DC61; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595764503,1595772653; mojo-session-id={"id":"d6aea7ece8bd41f45516e0f662f826a2","time":1595771411924}; mojo-trace-id=5; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595772672; __mta=188709399.1595764502994.1595764502994.1595764768326.2; _lxsdk_s=1738b635a70-dda-1eb-493%7C%7C11'

header = {}
header['User-Agent'] = user_agent
header['Cookie'] = cookie
response = requests.get(url, headers=header)

selector = lxml.etree.HTML(response.text)
movies = selector.xpath('//div[@class="movie-hover-info"]')
for movie in movies:
    movie_name = movie.xpath('./div[@class="movie-hover-title"]')[0].xpath('./span[@class="name"]/text()')
    movie_type = movie.xpath('./div[@class="movie-hover-title"]')[1].xpath('./span[@class="hover-tag"]/text()')
    movie_date = movie.xpath('./div[@class="movie-hover-title"]')[3].xpath('./span[@class="hover-tag"]/text()')

print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
title_list = soup.find_all('div', attrs={'class': 'movie-hover-info'}, limit=10)

result = []
result.append(['电影名称','电影类型','上映日期'])
for item in title_list:
    movie_name = item.find_all('div', attrs={'class': 'movie-hover-title'})[0].find('span',).text.strip()
    movie_type = item.find_all('div', attrs={'class': 'movie-hover-title'})[1].text.strip()
    movie_date = item.find_all('div', attrs={'class': 'movie-hover-title'})[3].text.strip()

    movie_item = [movie_name, re.split("\n+",movie_type)[1].strip(), re.split("\n+",movie_date)[1].strip()]
    result.append(movie_item)

movie_pd = pd.DataFrame(data=result)
movie_pd.to_csv('./movie1.csv', encoding='utf8', index=False, mode='a', header=False)
