import requests
from getpass import getpass

api_url = "https://suap.ifrn.edu.br/api/"

# AUTH BEGINS

user = input("user: ")
password = getpass()

data = {"username":user,"password":password}

response = requests.post(api_url+"v2/autenticacao/token/", json=data)
token = response.json()["access"]

headers = {
    "Authorization": f'Bearer {token}'
}
20

#AUTH ENDS
#
#GET SCORES BEGINS

#ano_letivo = str(input("Digite o ano letivo a ser consultado:\n"))
#periodo_letivo = str(input("Selecione o período (1 ou 2):\n"))

getscr = requests.get(api_url+f"v2/minhas-informacoes/boletim/2019/1", json=data, headers=headers)

#GET SCORES ENDS
#
#PRINT SCORES BEGINS

scrtable = getscore.json()["codigo_diaro"]

print(scrtable)