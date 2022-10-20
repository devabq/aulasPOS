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

def cUserFun(userInfo):
    cUserUrl = apiUrl + "/users/"
    cUser = requests.post(cUserUrl, json=userInfo)
    return cUser.json()

def rUserFun(userId):
    rUserUrl = apiUrl + "/users/" + str(userId)
    rUser = requests.get(rUserUrl)
    return rUser.json()

def uUserFun(userToUpd):
    uUserUrl = apiUrl + "/users/" + userToUpd
    uUser = requests.put(uUserUrl)
    print("work in progress")

def dUserFun(userToDel):
    dUser = apiUrl + "/users/" + userToDel
    dUser = requests.delete(dUserUrl)
    print("work in progress")

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
            updateUser()
        elif crudOption == "D":
            deleteUser()
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