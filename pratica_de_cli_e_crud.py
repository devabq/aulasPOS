import requests

apiUrl = "https://jsonplaceholder.typicode.com"

#################
# Listar usuários
#################

def option1ListUsers ():
    users = apiUrl + "/users/"
    getList = requests.get(users)
    return getList.json()

#############################
#Listar as tarefas do usuário
#############################

def option2ListUserTasks ():
    userId = input ("Listar as tarefas de qual usuário? \n")
    tasksFrom = apiUrl + "/users/" + userId + "/todos/"
    getTasks = requests.get(tasksFrom)
    return getTasks.json()

###########
#CRUD users
###########

#CRUD logic

def cUserFun(userInfo):
    cUserUrl = apiUrl + "/users/"
    cUser = requests.post(cUserUrl, json=userInfo)
    return cUser.json()

def rUserFun(userId):
    rUserUrl = apiUrl + "/users/" + str(userId)
    rUser = requests.get(rUserUrl)
    return rUser.json()

def uUserFun(userId, userInfo):
    uUserUrl = apiUrl + "/users/" + str(userId)
    uUser = requests.put(uUserUrl, json=userInfo)
    return uUser.json()

def dUserFun(userId):
    dUserUrl = apiUrl + "/users/" + str(userId)
    dUser = requests.delete(dUserUrl)
    return dUser.json()

#Crud CLI

def option3CrudUsers ():
    while True:
        crudOption = input("=========\nSelecione C/R/U/D ou B para voltar ao menu principal: \n")
        if crudOption == "C":
            userName = input("Digite o nome do usuário: \n")
            userEmail = input("Digite o email do usuário: \n")
            userInfo = {"name": userName, "email": userEmail}
            print(cUserFun(userInfo))
        elif crudOption == "R":
            userId = int(input("Digite a ID do usuário a ser lido:\n"))
            if userId > 10:
                print("=========\nUsuário não possui informações ou não existe!")
            elif 0 < userId < 11:
                print(rUserFun(userId))
            else:
                print("=========\nOcorreu um erro!")
        elif crudOption == "U":
            userId = int(input("Digite a ID do usuário a ser atualizado:\n"))
            if userId > 10:
                print("=========\nUsuário não possui informações ou não existe!")
            elif 0 < userId < 11:
                print(rUserFun(userId))
            else:
                print("=========\nOcorreu um erro!")
            userName = input("Digite o nome do usuário: \n")
            userEmail = input("Digite o email do usuário: \n")
            userInfo = {"name": userName, "email": userEmail}
            print(uUserFun(userId, userInfo))
        elif crudOption == "D":
            userId = int(input("Digite a ID do usuário a ser apagado:\n"))
            if userId > 10:
                print("=========\nUsuário não possui informações ou não existe!")
            elif 0 < userId < 11:
                print(dUserFun(userId))
            else:
                print("=========\nOcorreu um erro!")
        elif crudOption == "B":
            break
        else:
            print("=========\nOpção Inválida!")

###########
#CRUD tasks
###########

####
#CLI
####

while True:
    optionSelec = input("""=========
1: Listar usuários;  
2: Listar as tarefas do usuário;
3: CRUD users;
4: CRUD tasks;
Q: Sair do programa;
Digite o número da opção desejada: 
""")

    if optionSelec == "1":
        print(option1ListUsers())
    elif optionSelec == "2":
        print(option2ListUserTasks())
    elif optionSelec == "3":
        option3CrudUsers()
    elif optionSelec == "4":
        option4CrudTasks()
    elif optionSelec == "Q":
        break
    else:
        print("=========\nOpção inválida!")