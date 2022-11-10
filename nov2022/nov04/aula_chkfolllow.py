import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass


psswrd = getpass()

response = requests.put('https://api.github.com/users/dvcirilo/following',
                        auth=HTTPBasicAuth('paulo-albuquerque', psswrd))

print(response.text)
print(response)