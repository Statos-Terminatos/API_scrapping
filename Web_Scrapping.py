import requests
from bs4 import BeautifulSoup

response = requests.get("https://raw.githubusercontent.com/codelikerod/web-scraping/master/exemple1.html")
content = response.content
#print(content)

parser = BeautifulSoup(content, "html.parser")
# For tagging 
body = parser.body
p = body.p
#print(p.text)

head = parser.head
title = head.title
#print(title.text)

all_body = parser.find_all("body") 
p = all_body[0].find_all("p")
#print(p[0].text)

all_head = parser.find_all("head")
title = all_head[0].find_all("title")
#print(title[0].text)

# Extracting correct paragraph using ids
example2 = requests.get("https://raw.githubusercontent.com/codelikerod/web-scraping/master/exemple2.html")
content2 = example2.content
#print(content)
parser2 = BeautifulSoup(content2, "html.parser")

first_paragraph = parser2.find_all("p", id = "first")
#print(first_paragraph[0].text)

second_paragraph = parser2.find_all("p", id = "second")
#print(second_paragraph[0].text)

# Classes 
example3 = requests.get("https://raw.githubusercontent.com/codelikerod/web-scraping/master/exemple3.html")
content3 = example3.content
parser3 = BeautifulSoup(content3, "html.parser")
first_class1_paragraph = parser3.find_all("p", class_ = "class1")
#print(first_class1_paragraph[0].text)
#print(first_class1_paragraph[1].text)

# Example with CSS (Select method)
example4 = requests.get("https://raw.githubusercontent.com/codelikerod/web-scraping/master/exemple4.html")
content4 = example4.content
parser4 = BeautifulSoup(content4, "html.parser")
first_item = parser4.select(".first-item")

element_class2 = parser4.select(".class2")
first_class2_text = element_class2[0].text 
print(first_class2_text)

second_paragraph = parser4.select("#second")
second_text = second_paragraph[0].text
print(second_text)


# Associate selectors to CSS