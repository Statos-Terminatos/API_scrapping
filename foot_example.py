import requests
from bs4 import BeautifulSoup

response = requests.get("https://raw.githubusercontent.com/codelikerod/web-scraping/master/psg-vs-chelsea.html")
content = response.content
parser = BeautifulSoup(content, "html.parser")
#fautes = parser.find_all("tr", id = "fautes") using find_all
chelsea_fautes= parser.select("#fautes")[0].select("td")[1].text
print(chelsea_fautes)

psg_passes = parser.select("#passes")[0].select("td")[2].text
print(psg_passes)