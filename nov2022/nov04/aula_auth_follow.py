import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

response = requests.put('https://api.github.com/user/following/ClegiSilva',
                        auth=HTTPBasicAuth('paulo-albuquerque', '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'))

print(response.text)
print(response)