import subprocess

class Git:

    def __init__(self,repositorio =""):
        self.repositorio = repositorio

    def clonar(self):

        try:
            print("Clonando repositorio")
            proceso = subprocess.Popen(["git","clone",self.repositorio],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
            
            for linea in proceso.stdout:
                print(linea.strip())
            
            proceso.wait()

            if proceso.returncode != 0:
                print("Error al clonar el repositorio:")
                for linea in proceso.stderr:
                    print(linea.strip())
            else:
                print("Repositorio clonado correctamente")
            
        except Exception as ex:
            print(f"Ocurrio un error al copiar el repositorio {ex}")
    
    def status(self):

        proceso = subprocess.Popen(["git","status"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
            
        for linea in proceso.stdout:
            print(linea.strip())
            
        proceso.wait()

        if proceso.returncode != 0:
            print("Error al ejecutar el comando status:")
            for linea in proceso.stderr:
                print(linea.strip())
    
    def add(self):

        proceso = subprocess.Popen(["git","add","-A"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
            
        for linea in proceso.stdout:
            print(linea.strip())
            
        proceso.wait()

        if proceso.returncode != 0:
            print("Error al ejecutar el comando status:")
            for linea in proceso.stderr:
                print(linea.strip())

    def commit(self,texto):

        proceso = subprocess.Popen(["git","commit","-m",f'"{texto}"'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
            
        for linea in proceso.stdout:
            print(linea.strip())
            
        proceso.wait()

        if proceso.returncode != 0:
            print("Error al ejecutar el comando status:")
            for linea in proceso.stderr:
                print(linea.strip())
    
    def usuario(self,usuario):

        proceso = subprocess.Popen(["git","config","--global","user.name",usuario],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
            
        for linea in proceso.stdout:
            print(linea.strip())
            
        proceso.wait()

        if proceso.returncode != 0:
            print("Error al ejecutar el comando status:")
            for linea in proceso.stderr:
                print(linea.strip())
    
    def correo(self,email):

        proceso = subprocess.Popen(["git","config","--global","user.email",email],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
            
        for linea in proceso.stdout:
            print(linea.strip())
            
        proceso.wait()

        if proceso.returncode != 0:
            print("Error al ejecutar el comando status:")
            for linea in proceso.stderr:
                print(linea.strip())
    
    def master(self,master):

        proceso = subprocess.Popen(["git","push","origin",master],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
            
        for linea in proceso.stdout:
            print(linea.strip())
            
        proceso.wait()

        if proceso.returncode != 0:
            print("Error al ejecutar el comando status:")
            for linea in proceso.stderr:
                print(linea.strip())
    

    def log(self):

        proceso = subprocess.Popen(["git","log"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
            
        for linea in proceso.stdout:
            print(linea.strip())
            
        proceso.wait()

        if proceso.returncode != 0:
            print("Error al ejecutar el comando status:")
            for linea in proceso.stderr:
                print(linea.strip())