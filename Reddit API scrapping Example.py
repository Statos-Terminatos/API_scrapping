# import the libraries for API scrapping 
import requests 
import requests.auth
from authorization_details import token
from authorization_details import secret 

client_auth = requests.auth.HTTPBasicAuth(token, secret)
print(token)
print(secret)