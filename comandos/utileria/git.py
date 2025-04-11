from lib.utileria.git import Git
from lib.utileria.validaciones import validarRuta,validarTexto
import os

def git(rutaBase,args):

    argumentos = args.split()
    comando = argumentos[0]

    if comando == "-c":
        ruta = argumentos[1]

        if validarRuta(ruta):

            directorioRaiz = os.getcwd()
            scriptPath = os.path.abspath(rutaBase)
            #scriptDir = os.path.dirname(scriptPath)
            os.chdir(scriptPath)

            gt =  Git(ruta)
            gt.clonar()

            os.chdir(directorioRaiz)

        else:
            print("La ruta introducida no es valida")
    
    if comando == "-s":

        directorioRaiz = os.getcwd()
        scriptPath = os.path.abspath(rutaBase)
        os.chdir(scriptPath)

        gt =  Git()
        gt.status()

        os.chdir(directorioRaiz)
    
    if comando == "-a":
        
        directorioRaiz = os.getcwd()
        scriptPath = os.path.abspath(rutaBase)
        os.chdir(scriptPath)

        gt =  Git()
        gt.add()

        os.chdir(directorioRaiz)

    if comando == "-m":
        
        if len(argumentos) >= 2: 

            comentario  = ""

            for palabra in argumentos[1:]:
                comentario += palabra + " "

            if validarTexto(comentario):

                directorioRaiz = os.getcwd()
                scriptPath = os.path.abspath(rutaBase)
                os.chdir(scriptPath)

                gt =  Git()
                gt.commit(comentario+" ")

                os.chdir(directorioRaiz)
        
            else:
                print("Solo puedes introdicir numeros y letras algunos caracteres permitidos")
        
        else:
            print("Debes de agregar un comentario")

    if comando == "-u":
        usuario = argumentos[1]

        directorioRaiz = os.getcwd()
        scriptPath = os.path.abspath(rutaBase)
        os.chdir(scriptPath)

        gt =  Git()
        gt.usuario(usuario)

        os.chdir(directorioRaiz)

    if comando == "-e":
        email = argumentos[1]

        directorioRaiz = os.getcwd()
        scriptPath = os.path.abspath(rutaBase)
        os.chdir(scriptPath)

        gt =  Git()
        gt.correo(email)

        os.chdir(directorioRaiz)
    
    if comando == "-o":
        
        master = argumentos[1]

        directorioRaiz = os.getcwd()
        scriptPath = os.path.abspath(rutaBase)
        os.chdir(scriptPath)

        gt =  Git()
        gt.master(master)

        os.chdir(directorioRaiz)
    
    if comando == "-l":

        directorioRaiz = os.getcwd()
        scriptPath = os.path.abspath(rutaBase)
        os.chdir(scriptPath)

        gt =  Git()
        gt.log()

        os.chdir(directorioRaiz)