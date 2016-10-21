#!/usr/bin/env python
import urllib
import pandas as pd
from bs4 import BeautifulSoup
import json
import requests
import re
import time

df1 = pd.read_csv("/users/Sheena/Desktop/DSI/Capstone/assets/weather_rep.csv")

df1.dates = pd.to_datetime(df1.dates, format="%d/%m/%y")

df1["month"]=df1['dates'].dt.strftime('%m')
df1["day"]=df1['dates'].dt.strftime('%d')

rain = []
snow = []

len(df1)

#RUN ON DAY1 (FRIDAY OR SAT)
for y,m,d,state,city in zip(df1["year"].tolist(),df1["month"].tolist(),
df1["day"].tolist(),df1["state"].tolist(),df1["city"].tolist()):
    api_base_url = 'http://api.wunderground.com/api/ecf23b1cb8c40db8/history_%s%s%s/q/%s/%s.json'%(y,m,d,state,city)
    response = json.loads(requests.get(api_base_url).text)
    snow.append(response["history"]["dailysummary"][0]["snow"])
    rain.append(response["history"]["dailysummary"][0]["rain"])
    time.sleep(7)

print len(rain)
print len(snow)

df1["rain"]=rain
df1["snow"]=snow

df1.to_csv("/users/Sheena/Desktop/DSI/Capstone/assets/weather2.csv",index=False,encoding="utf-8")