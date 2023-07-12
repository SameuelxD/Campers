import core
import os
infoAcudientes= {"data":[]}
def LoadInfoAcudientes():
    global infoAcudientes
    if (core.CheckFile("acudientes.json")):
        infoAcudientes = core.LoadInfo("acudientes.json")
    else:
        core.AddInfo("acudientes.json",infoAcudientes)
def MainMenu():
    Passive = True
    os.system("cls")
    print('+','-'*55,'+')
    print("|{:^16}{}{:^15}|".format(' ','GESTION DE ACUDIENTES',' '))
    print('+','-'*55,'+')
    print("1. Registrar Acudiente")
    print("2. Buscar Acudiente")
    print("3. Editar Acudiente")
    print("4. Eliminar Acudiente")
    print("5. Regresar menu principal")
    opcion =int(input(":)_"))
    if (opcion == 1):
        while(Passive):
            id = (input("Digite el Id del Camper con Acudiente a Registrar:"))
            for i,item in enumerate(infoCampers["data"]):
                if id in item["Id"]:
                    edad=int(item["Edad"])
                    if(edad<18):
                        acudiente ={
                            "Id":input("Digite el Id del Acudiente: "),
                            "Nombre":input("Digite el Nombre del Acudiente: "),
                            "Apellido":input("Digite el Apellido del Acudiente: "),
                            "Parentezco":input("Digite el Parentezco con el Camper: ")
                        }
                        infoAcudientes["data"].append(acudiente)
                        core.AddInfo("acudientes.json",acudiente)
                        Passive=bool(input("Digite un valor Alphanumerico para volver a Ingresar un Acudiente o Presione Enter para Salir al Menu Principal --> "))
                    else:
                        print("¡ERROR! El Camper no necesita Regitrar Acudiente,solo para menores de Edad ")
            Passive=bool(input("Digite un valor Alphanumerico para volver a Ingresar un Acudiente o Presione Enter para Salir al Menu Principal --> "))
        
        