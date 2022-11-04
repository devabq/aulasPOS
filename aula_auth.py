import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

user = input("user: ")
password = getpass()
  
response = requests.get('https://api.github.com/user',
            auth = HTTPBasicAuth('paulo-albuqquerque', password))
  
print(response.text)
print(response)
#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