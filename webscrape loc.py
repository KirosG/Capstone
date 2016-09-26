#!/usr/bin/env python
import urllib
import pandas as pd
from bs4 import BeautifulSoup
dates=[]
teams=[]

for i in range(2013,2016):
    url = 'http://www.pro-football-reference.com/years/%s/games.htm'%i
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html,"html.parser")

    for tr in soup.find_all('tr')[1:273]:
        try:
            d = tr.find('td',{"data-stat":"game_date"}).get("csk")
            loc = tr.find('td',{"data-stat":"game_location"}).renderContents()
            if loc == "@":
                home = tr.find('td',{"data-stat":"loser"}).getText()
            else:
                home = tr.find('td',{"data-stat":"winner"}).getText()

            dates.append(d)
            teams.append(home)

        except:
            pass

    for tr in soup.find_all('tr')[273:]:
        try:
            d = tr.find('td',{"data-stat":"game_date"}).renderContents()
            d = d + i
            loc = tr.find('td',{"data-stat":"game_location"}).renderContents()
            if loc == "@":
                home = tr.find('td',{"data-stat":"loser"}).getText()
            elif loc == "N":
                home = "Superbowl %s" %i
            else:
                home = tr.find('td',{"data-stat":"winner"}).getText()

            dates.append(d)
            teams.append(home)

        except:
            pass

df = pd.DataFrame({'dates' : dates,'location' : teams})
df.to_csv("/users/Sheena/Desktop/indeed.csv",sep=',', encoding='utf-8')
