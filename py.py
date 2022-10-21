def option3Crudtasks ():
    while True:
        crudOption = input("=========\nSelecione C/R/U/D ou B para voltar ao menu principal: \n")
        if crudOption == "C":
            taskName = input("Digite o nome do Tarefa: \n")
            taskEmail = input("Digite o email do Tarefa: \n")
            taskInfo = {"name": taskName, "email": taskEmail}
            print(ctaskFun(taskInfo))
        elif crudOption == "R":
            taskId = int(input("Digite a ID da Tarefa a ser lido:\n"))
            if taskId > 10:
                print("=========\nTarefa não possui informações ou não existe!")
            elif 0 < taskId < 11:
                print(rtaskFun(taskId))
            else:
                print("=========\nOcorreu um erro!")
        elif crudOption == "U":
            taskId = int(input("Digite a ID da Tarefa a ser atualizado:\n"))
            if taskId > 10:
                print("=========\nTarefa não possui informações ou não existe!")
            elif 0 < taskId < 11:
                print(rtaskFun(taskId))
            else:
                print("=========\nOcorreu um erro!")
            taskName = input("Digite o nome do Tarefa: \n")
            taskEmail = input("Digite o email do Tarefa: \n")
            taskInfo = {"name": taskName, "email": taskEmail}
            print(utaskFun(taskId, taskInfo))
        elif crudOption == "D":
            taskId = int(input("Digite a ID da Tarefa a ser apagado:\n"))
            if taskId > 10:
                print("=========\nTarefa não possui informações ou não existe!")
            elif 0 < taskId < 11:
                print(dtaskFun(taskId))
            else:
                print("=========\nOcorreu um erro!")
        elif crudOption == "B":
            break
        else:
            print("=========\nOpção Inválida!")