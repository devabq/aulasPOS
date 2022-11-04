import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

user = input("user: ")
password = getpass()
  
response = requests.get('https://api.github.com/user',
            auth = HTTPBasicAuth('paulo-albuquerque', password))
  
print(response.text)
print(response)
#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
