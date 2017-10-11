# import the libraries for API scrapping 
import requests 
import requests.auth
from authorization_details import * 

client_auth = requests.auth.HTTPBasicAuth(token, secret)
post_data = {"grant_type": "password", "username":username, "password":password}
headers ={'User-agent':'Formation API'}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth = client_auth, data = post_data, 
                        headers = headers)
print(response.json()["access_token"])

authorization = "bearer " + response.json()["access_token"]
print(authorization)
headers = {"authorization":authorization, "User-agent": "Formation API"}
params = {"t":"week"}
# Get top reddit posts on topic python for the last week
response = requests.get("https://oauth.reddit.com/r/python/top", headers = headers, params = params)
python_top = response.json()
print(python_top)