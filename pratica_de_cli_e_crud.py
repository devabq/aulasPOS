import requests

apiUrl = "https://jsonplaceholder.typicode.com"

##################
# Listar usuários
#################

def option1 ():
    users = apiUrl + "/users/"
    getList = requests.get(users)
    print(getList.json())

#############################
#Listar as tarefas do usuário
#############################

def option2 ():
    userId = input ("Listar as tarefas de qual usuário? ")
    tasksFrom = apiUrl + "/users/" + userId + "/todos/"
    getTasks = requests.get(tasksFrom)
    print(getTasks.json())

###########
#CRUD users
###########

def option3 ():
    while True:
        crudOption = input("Selecione C/R/U/D: ")
        if optionSelec == "C":
            createUser()
        elif optionSelec == "R":
            readUser()
        elif optionSelec == "U":
            updateUser()
        elif optionSelec == "D":
            deleteUser()
        else:
            break

####
#CLI
####

while True:
    optionSelec = int(input("""=========
    1: Listar usuários;  
    2: Listar as tarefas do usuário;
    3: CRUD users;
    Digite o número da opção desejada: """))

    if optionSelec == 1:
        option1()
    elif optionSelec == 2:
        option2()
    elif optionSelec == 3:
        option3()
    elif optionSelec == 4:
        option4()
    else:
        break