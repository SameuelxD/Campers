# El centro de entrenamiento de software campus land desea realizar un programa que le permita llevar el control de los candidatos interesados a participar en su programa de entrenamiento.Campus desea realizar un registro previo de los participantes; La informacion que se contempla por cada participante es la siguiente: Nro Id,Nombres,Apellidos,Edad,Correo Electronico,Ciudad de Origen,Estado Civil,Genero,Nro Telefonico.
# Los campers que son menores de edad,deben registrar informacion de acudientes,con la siguiente informacion: Identificacion del acudiente,Nombre del acudiente y parentezco.
# La informacion ingresada debe ser almacenada de forma local
import os
import campers
import acudientes
if __name__ == "__main__":
    Activate = True
    DataCampers={'data':[]}
    DataAcudientes={'data':[]}
    opcion=0
    while(Activate):
        os.system("cls")
        print('+','-'*55,'+')
        print("|{:^20}{}{:^24}|".format(' ','Menu Pricipal',' '))
        print('+','-'*55,'+')
        print("1. Gestion de Campers")
        print("2. Gestion de Acudientes")
        print("3. Finalizar")
        opcion=int(input("Digite la Opcion: "))
        if(opcion==1):
            campers.LoadInfoCampers()
            campers.MainMenu()    
        elif(opcion==2):
            acudientes.LoadInfoAcudientes()
            acudientes.MainMenu()
        elif(opcion==3):
            Activate=False