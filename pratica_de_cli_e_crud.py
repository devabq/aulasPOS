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

#Da pra otimizar o /users/ url and stuff mas to com preguiça

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

#CRUD CLI

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

#CRUD logic

wip = "work in progress"
tasksUrl = apiUrl + "/todos/"

def cTaskFun(taskInfo):
    cTask = requests.post(tasksUrl, json=taskInfo)
    return cTask.json()

def rTaskFun(taskId):
    rTaskUrl = taskId + str(uTaskId)
    rTask = requests.get(rTaskUrl)
    return rTask.json()

def uTaskFun(taskId, taskInfo):
    uTaskUrl = tasksUrl + str(taskId)
    uTask = requests.put(uTaskUrl, json=taskInfo)
    return uTask.json()
def dTaskFun(taskId):
    dTaskUrl = tasksUrl + str(taskId)
    dTask = requests.delete(dTaskUrl)
    return dTask.json()

#CRUD CLI

def option4CrudTasks():
    while True:
        crudOption = input("=========\nSelecione C/R/U/D ou B para voltar ao menu principal: \n")
        if crudOption == "C":
            taskName = input("Digite o nome do Tarefa: \n")
            taskDesc = input("Digite a descrição do Tarefa: \n")
            taskInfo = {"name": taskName, "desc": taskDesc}
            print(cTaskFun(taskInfo))
        elif crudOption == "R":
            taskId = int(input("Digite a ID da Tarefa a ser lido:\n"))
            if taskId > 10:
                print("=========\nTarefa não possui informações ou não existe!")
            elif 0 < taskId < 11:
                print(rTaskFun(taskId))
            else:
                print("=========\nOcorreu um erro!")
        elif crudOption == "U":
            taskId = int(input("Digite a ID da Tarefa a ser atualizado:\n"))
            taskName = input("Digite o nome da Tarefa: \n")
            taskDesc = input("Digite a descrição da Tarefa: \n")
            taskInfo = {"name": taskName, "desc": taskDesc}
            print(uTaskFun(taskId, taskInfo))
        elif crudOption == "D":
            taskId = int(input("Digite a ID da Tarefa a ser apagado:\n"))
            print(dTaskFun(taskId))
        elif crudOption == "B":
            break
        else:
            print("=========\nOpção Inválida!")

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