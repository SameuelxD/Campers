import core
import os
infoAcudientes= {"data":[]}
def LoadInfoAcudientes():
    global infoAcudientes
    if (core.CheckFile("Acudientes.json")):
        infoAcudientes = core.LoadInfo("acudientes.json")
    else:
        core.AddInfo("acudientes.json",infoAcudientes)

def MainMenu():
    os.system("clear")
    Passive = True
    os.system("clear")
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
        Acudiente ={
            "Id":int(input("Digite el Id del Acudiente: ")),
            "Nombre":input("Digite el Nombre del Acudiente: "),
            "Apellido":input("Digite el Apellido del Acudiente: "),
            "Parentezco":input("Digite el Parentezco con el Camper: ")
        }
        infoAcudientes["data"].append(Acudiente)
        core.AddInfo("Acudientes.json",Acudiente)
        