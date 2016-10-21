#!/usr/bin/env python
import urllib
import pandas as pd
from bs4 import BeautifulSoup
import json
import requests
import re
import time

df1 = pd.read_csv("/users/Sheena/Desktop/DSI/Capstone/assets/game_location.csv")
df2 = pd.read_csv("/users/Sheena/Desktop/DSI/Capstone/assets/location.csv")

city=[]
state=[]
offense=[]

for x in df1.values:
    for y in df2.values:
        if x[1] == y[2]:
            city.append(y[3])
            state.append(y[4])
            offense.append(y[0])

df1["city"] = city
df1["state"] = state
df1["offense"] = offense

df1.dates = pd.to_datetime(df1.dates)

df1['year'] = df1['dates'].dt.year
df1["month"]=df1['dates'].dt.strftime('%m')
df1["day"]=df1['dates'].dt.strftime('%d')

rain = []
snow = []

len(df1)
#im going to split my data into 3 parts just to be sure. I can only run 500 requests a day
#for the wunderground api --> i have 801 rows -> max of 10 requests per minute delay 1 second
dfs1 = df1.iloc[0:300,:]
dfs2 = df1.iloc[300:600,:]
dfs3 = df1.iloc[600:,:]

##RUN ON DAY1 (FRIDAY OR SAT)
#for y,m,d,state,city in zip(dfs1["year"].tolist(),dfs1["month"].tolist(),
#dfs1["day"].tolist(),dfs1["state"].tolist(),dfs1["city"].tolist()):
#    api_base_url = 'http://api.wunderground.com/api/ecf23b1cb8c40db8/history_%s%s%s/q/%s/%s.json'%(y,m,d,state,city)
#    response = json.loads(requests.get(api_base_url).text)
#    snow.append(response["history"]["dailysummary"][0]["snow"])
#    rain.append(response["history"]["dailysummary"][0]["rain"])
#    time.sleep(7)

##RUN ON DAY2 (SATURDAY or SUNDAY)
#for y,m,d,state,city in zip(dfs2["year"].tolist(),dfs2["month"].tolist(),
#dfs2["day"].tolist(),dfs2["state"].tolist(),dfs2["city"].tolist()):
#    api_base_url = 'http://api.wunderground.com/api/ecf23b1cb8c40db8/history_%s%s%s/q/%s/%s.json'%(y,m,d,state,city)
#    response = json.loads(requests.get(api_base_url).text)
#    snow.append(response["history"]["dailysummary"][0]["snow"])
#    rain.append(response["history"]["dailysummary"][0]["rain"])
#    time.sleep(7)

##DAY 3 (SUN OR MONDAY)
for y,m,d,state,city in zip(dfs3["year"].tolist(),dfs3["month"].tolist(),
dfs3["day"].tolist(),dfs3["state"].tolist(),dfs3["city"].tolist()):
    api_base_url = 'http://api.wunderground.com/api/ecf23b1cb8c40db8/history_%s%s%s/q/%s/%s.json'%(y,m,d,state,city)
    response = json.loads(requests.get(api_base_url).text)
    snow.append(response["history"]["dailysummary"][0]["snow"])
    rain.append(response["history"]["dailysummary"][0]["rain"])
    time.sleep(7)

print len(rain)
print len(snow)
