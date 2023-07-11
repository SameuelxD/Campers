import core
import os
infoCampers= {"data":[]}
def LoadInfoCampers():
    global infoCampers
    if (core.CheckFile("campers.json")):
        infoCampers = core.LoadInfo("campers.json")
    else:
        core.AddInfo("campers.json",infoCampers)
def MainMenu():
    Passive=True 
    os.system("cls")
    print('+','-'*55,'+')
    print("|{:^16}{}{:^15}|".format(' ','GESTION DE CAMPERS',' '))
    print('+','-'*55,'+')
    print("1. Registrar Camper")
    print("2. Buscar Camper")
    print("3. Editar Camper")
    print("4. Eliminar Camper")
    print("5. Regresar menu principal")
    opcion =int(input("Digite Opcion: "))
    if (opcion == 1):
        while(Passive):
            print('+','-'*49,'+')
            print("|{:^16}{}{:^15}|".format(' ','REGISTRAR CAMPERS',' '))
            print('+','-'*49,'+')
            camper ={
                "Id":(input("Digite el Id del Camper: ")),
                "Nombre":input("Digite el Nombre del Camper: "),
                "Apellido":input("Digite el Apellido del Camper: "),
                "Edad":int(input("Digite la Edad del Camper: ")),
                "Email":input("Digite el Correo Electronico del Camper: "),
                "Ciudad-Origen":input("Digite la Ciudad de Origen del Camper: "),
                "Estado-Civil":input("Digite el Estado Civil del Camper: "),
                "Genero":input("Digite el Genero del Camper: "),
                "Telefono":int(input("Digite el Telefono del Camper: "))
            }
            infoCampers["data"].append(camper)
            core.AddInfo("campers.json",camper)
            Passive=bool(input("Digite un valor Alphanumerico para volver a Ingresar un Camper o Presione Enter para Salir al Menu Principal --> "))
    
    elif (opcion == 2):
        while(Passive):
            os.system("cls")
            print('+','-'*49,'+')
            print("|{:^16}{}{:^15}|".format(' ','BUSCADOR DE CAMPERS',' '))
            print('+','-'*49,'+')
            id = (input("Digite el Id del Camper a Buscar:"))
            for i,item in enumerate(infoCampers["data"]):
                if id in item["Id"]:
                    print(f'Id Camper : {item["Id"]}')
                    print(f'Nombre Camper : {item["Nombre"].upper()}')
                    print(f'Email Camper : {item["Email"]}')
            Passive=bool(input("Digite un valor Alphanumerico para volver a Buscar un Camper o Presione Enter para Salir al Menu Principal --> "))

    elif (opcion == 3):
        while(Passive):
            os.system("cls")
            print('+','-'*49,'+')
            print("|{:^16}{}{:^15}|".format(' ','EDITAR CAMPERS',' '))
            print('+','-'*49,'+')
            id = input("Digite el Id del Camper a Editar: ")
            for i,item in enumerate(infoCampers["data"]):
                if id in item["Id"]:
                    item["Nombre"] = input("Digite un Nuevo Nombre para el Camper o Presione Enter para Omitir: ") or item["Nombre"]
                    item["Email"] = input("Digite un Nuevo Email para el Camper o Presione Enter para Omitir: ") or item["Email"]
                    core.EditarData("campers.json",infoCampers)
            Passive=bool(input("Digite un valor Alphanumerico para volver a Editar un Camper o Presione Enter para Salir al Menu Principal --> "))

    elif (opcion == 4):
        while(Passive):
            os.system("cls")
            print('+','-'*49,'+')
            print("|{:^16}{}{:^15}|".format(' ','ELIMINAR CAMPERS',' '))
            print('+','-'*49,'+')
            id = input("Digite el Id del Cliente a Eliminar: ")
            for i,item in enumerate(infoCampers["data"]):
                if id in item["Id"]:
                    itemDel = infoCampers["data"].pop(i)
                    core.EditarData("campers.json",infoCampers)
            Passive=bool(input("Digite un valor Alphanumerico para volver a Eliminar un Camper o Presione Enter para Salir al Menu Principal --> "))

    elif (opcion == 5):
        Passive = False
    if Passive:
        MainMenu()
    