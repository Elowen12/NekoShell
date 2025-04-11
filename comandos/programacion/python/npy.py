from lib.programacion.python.clase import Class
from lib.utileria.validaciones import validarNombre,validarNombreArchivo,validarRuta
import os
import signal
import subprocess
import io

def npy(rutaBase,virtual,envScripts,args):

    argumentos = args.split()
    comando = argumentos[0]

    if comando == "-c":
        
        nombre = argumentos[1]

        if validarNombre(nombre):
        
            if not os.path.exists(rutaBase+nombre+".py"):
                archivo = Class(rutaBase+nombre+".py",nombre)
            
                resultado = archivo.crear()

                if resultado:
                    print("Clase creada correctamente.")
                else:
                    print("No se puedo crear la clase solicitada")
            else:
                print("El archivo ya existe en el directorio")

        else:
            print("El nombre o la ruta no son validos")
    
    elif comando == "-e":
        
        script = argumentos[1]

        if validarNombreArchivo(script):
        
            extension = os.path.splitext(script)
            
            if extension[1] == ".py":
                
                try:
                    def monitoreoteclas(signum,frame):

                        if proceso:
                            print("Script interrumpido")
                            proceso.terminate()
                
                    signal.signal(signal.SIGINT,monitoreoteclas)

                    directorioRaiz = os.getcwd()
                    scriptPath = os.path.abspath(rutaBase)
                    #scriptDir = os.path.dirname(scriptPath)
                    os.chdir(scriptPath)
                    if virtual:
                        proceso = subprocess.Popen([envScripts+"/python.exe",rutaBase+script])
                        proceso.wait()
                    else:
                        proceso = subprocess.Popen(["python",rutaBase+script])
                        proceso.wait()

                        proceso = None
                        os.chdir(directorioRaiz)
                except Exception as e:
                        print("No se pudo ejecutar el script, revisa la ruta del archivo." +str(e))


            else:
                print("La extencion del archivo no es valida")

        else:
            print("El script ingresado no es valido")

    elif comando == "-v":
        virtual = argumentos[1]

        if validarNombre(virtual):
              
            try:
                print("Creando entorno virtual")
                proceso = subprocess.Popen(['python','-m','venv',rutaBase+virtual])
                proceso.wait()
                print("Entorno virtual creado")
            except:
                print("Problemas al crear el entorno virtual")

        else:
            print("El nombre del entorno virtual no es valido.")
    
    elif comando == "-ev":    
        virtual = argumentos[1]

        if os.path.exists(rutaBase+virtual):
            
            scripts = rutaBase + virtual+"/Scripts"
            print("Entorno virtual activado")
            return {"proceso":"virtual","env":True,"envScripts":scripts}

        else:
            print("El entorno virtual no existe")

    elif comando == "-i":
        paquete = argumentos[1]

        if virtual:
            pip = envScripts +"/pip.exe"
            os.system(f"{pip} install {paquete}")
        else:
            os.system(f"pip install {paquete}")

