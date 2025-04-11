from lib.sistema.sistema import SO
from colorama import Fore, Style, init
import os

def hora():
    
    sistemaOperativo = SO()
    hora = sistemaOperativo.hora()

    print(f"{Fore.YELLOW}La hora actual es: {hora}")

def fecha():

    sistemaOperativo = SO()
    fecha = sistemaOperativo.fecha()

    print(f"{Fore.YELLOW}La fecha actual es: {fecha}")

def ls(args,rutaBase):

    argumentos = args.split()
    sistema = SO()

    if len(argumentos) > 0:
            

        try:

            contenido = sistema.ls(argumentos[0])

            for con in contenido:
                print(f"{Fore.BLUE}-> {con}")
            
        except:
            print("La ruta proporcinada no es valida.")

    else:
            
        try:

            contenido = sistema.ls(rutaBase)

            for con in contenido:
                print(f"{Fore.BLUE}-> {con}")
            
        except:
                print("La ruta proporcinada no es valida.")

def cd(args,rutaBase):

    argumentos = args.split()

    if len(argumentos) > 0:
            
        try:
            
            argumento = argumentos[0]

            if os.path.isabs(argumento):

                if os.path.isdir(argumento):
                        
                    return {"base":True,"argumento":argumento}
                   

                else:
                    return  {"error":True,"contenido":"Ruta no valida"}

            else:
                rutaBase = rutaBase + argumento +"/"
                path = rutaBase

                if os.path.isdir(path):

                    return {"base":False,"argumento":path}

                else:
                    return  {"error":True,"contenido":"Ruta no valida 2"}
            
        except Exception as e:
            return  {"error":True,"contenido":e}
        
    else:
        
        return  {"error":True,"contenido":"Debes proporcionar una ruta para mostrar su contenido."}


def back(rutaBase):
    
    path = rutaBase

    if "/" in path:
        partes = path.rsplit("/", 1)  # Divide desde el final

        #print(partes)

        if partes[len(partes)-1] == "" and partes[0] != "":
            partes.remove("")
            
            #print(partes)

            partes = partes[0].rsplit("/", 1)

            #print(partes)

            if partes[0] == "":

                path = "/"
                
            elif ":" in partes[0] and len(partes[0]) == 2:
                path = partes[0] + "/"
                
            else:
                path = partes[0]

            
        elif len(partes) >= 2 and partes[0] != "" and ":" not in partes[0]:

            #print(partes)

            path = partes[0]
            
        elif len(partes) >= 2 and partes[0] != "" and ":" in partes[0]:

            #print(partes)

            path = partes[0] + "/"
            
        else:
            path = "/"

    else:
        path = "/"  # Maneja el caso en que ya no hay más barras

    return path


    

