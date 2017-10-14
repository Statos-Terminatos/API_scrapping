import requests
from bs4 import BeautifulSoup

page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.WeIXlUqCzq0")
content = page.content
parser = BeautifulSoup(content, "html.parser")
forecast  = parser.find_all(id = "seven-day-forecast")
items = forecast[0].find_all(class_="tombstone-container")
today = items[0]
img = today.find("img")
#print(today.prettify())

weather_forecast = []
for item in items:
    temp = {}
    temp["period"] = item.find(class_="period-name").get_text()
    temp["title"] = item.find("img")["title"]
    temp["description"] = item.find(class_="short-desc").get_text()
    temp["temperature"] =item.find(class_="temp").get_text()
    weather_forecast.append(temp)
#print(weather_forecast)

#using select
period_tags = forecast[0].select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
short_descr = [desc.get_text() for desc in forecast[0].select(".tombstone-container .short-desc")]
description = [d['title'] for d in forecast[0].select(".tombstone-container img")]
print(description)