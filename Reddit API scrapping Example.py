# import the libraries for API scrapping 
import requests 
import requests.auth
from authorization_details import * 
import json

client_auth = requests.auth.HTTPBasicAuth(token, secret)
post_data = {"grant_type": "password", "username":username, "password":password}
headers ={'User-agent':'Formation API'}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth = client_auth, data = post_data, 
                        headers = headers)

authorization = "bearer " + response.json()["access_token"]
headers = {"authorization":authorization, "User-agent": "Formation API"}
params = {"t":"week"}
# Get top reddit posts on topic python for the last week
response = requests.get("https://oauth.reddit.com/r/python/top", headers = headers, params = params)
python_top = response.json()

# Obtain most upvoted posts
all_articles = python_top["data"]["children"]
# Extract the keys: "id" and "ups"
ids = []   

for article in all_articles:
    new_data = {}
    temp = article["data"]
    new_data["id"] = temp["id"]
    new_data["votes"] = temp["ups"]
    ids.append(new_data)

#print(ids) 

#loop to find the unique most upvoted article
most_pop_id = ""
nb_votes = 0

for article in all_articles:
    temp = article["data"]
    if temp["ups"]>= nb_votes:
        most_pop_id = temp["id"]
        nb_votes = temp["ups"]

print("Most popular article id is: ", most_pop_id, "with total number of votes", nb_votes)

reponse_comments = requests.get("https://oauth.reddit.com/r/python/comments/75ia74",
                                 headers = headers, params = params)
all_comments = reponse_comments.json()

comment_content = ""
comment_id = ""
comment_votes = 0

comments_list = all_comments[1]["data"]["children"]
for comment in comments_list:
    temp = comment["data"] 
    if temp["ups"] >= comment_votes:
        comment_id = temp["id"]
        comment_votes = temp["ups"]
        comment_content = temp["body"]

print(comment_content, comment_id, comment_votes)