import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.86948000000007&lon=-122.25928999999996#.XhelV0dKhPY')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id = 'seven-day-forecast-body')
#print(week)
items = week.find_all(class_ = 'tombstone-container') #class_ <- bc 'class' is rereved
#print(items[0].find(class_='period-name').get_text()) #biore items 0, czyli te opcje z today, potem biore klase w ktorej zapisane jest wlasnie dzien,
# i wyswietlam nazwe tego dnai, bez get_text() wyswietli mi caly paragraf

print(items)

period_names=[item.find(class_='period-name').get_text() for item in items]
short_descriptions=[item.find(class_='short-desc').get_text() for item in items]
temps=[item.find(class_='temp').get_text() for item in items]

print(period_names)
print(short_descriptions)
print(temps)

weather_stuff= pd.DataFrame({
    'period': period_names,
    'description': short_descriptions,
    'temperature': temps
})

print(weather_stuff)

weather_stuff.to_csv('weather.csv')