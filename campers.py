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
    os.system("clear")
    Passive = True
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^16}{}{:^15}|".format(' ','GESTION DE CAMPERS',' '))
    print('+','-'*55,'+')
    print("1. Registrar Camper")
    print("2. Buscar Camper")
    print("3. Editar Camper")
    print("4. Eliminar Camper")
    print("5. Regresar menu principal")
    opcion =int(input(":)_"))
    if (opcion == 1):
        camper ={
            "Id":int(input("Digite el Id del Camper: ")),
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
        
    """elif (opcion == 2):
        os.system("clear")
        print('+','-'*49,'+')
        print("|{:^16}{}{:^15}|".format(' ','BUSCADOR DE CLIENTES',' '))
        print('+','-'*49,'+')
        cliSearch = input("Ingrese el codigo del cliente a buscar:")
        for i,item in enumerate(diccCliente["data"]):
            if cliSearch in item["id"]:
                print(f'Id cliente : {item["id"]}')
                print(f'Nombre cliente : {item["nombre"].upper()}')
                print(f'Email cliente : {item["email"]}')
        os.system("pause")
    elif (opcion == 3):
        os.system("clear")
        print('+','-'*49,'+')
        print("|{:^16}{}{:^15}|".format(' ','EDICION DE CLIENTES',' '))
        print('+','-'*49,'+')
        cliSearch = input("Ingrese el codigo del cliente a editar:")
        for i,item in enumerate(diccCliente["data"]):
            if cliSearch in item["id"]:
                item["nombre"] = input("Ingrese en nuevo nombre o presione enter para omitir :") or item["nombre"]
                item["email"] = input("Ingrese en nuevo email o presione enter para omitir :") or item["email"]
                core.EditarData("clientes.json",diccCliente)
    elif (opcion == 4):
        os.system("clear")
        print('+','-'*49,'+')
        print("|{:^16}{}{:^15}|".format(' ','ELIMINACION DE CLIENTES',' '))
        print('+','-'*49,'+')
        cliSearch = input("Ingrese el codigo del cliente a editar:")
        for i,item in enumerate(diccCliente["data"]):
            if cliSearch in item["id"]:
                itemDel = diccCliente["data"].pop(i)
                core.EditarData("clientes.json",diccCliente)
                # os.system("pause")
                # core.crearInfo("clientes.json",itemDel)

    elif (opcion == 5):
        Passive = False
    if Passive:
        MainMenu()

    """