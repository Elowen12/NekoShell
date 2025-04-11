import cmd
from colorama import Fore, Style, init
import argparse

from  comandos.sistema.nversion import nversion
from comandos.sistema.usuarios import usuario, usuarios
from comandos.sistema.consola import limpiar
from comandos.sistema.so import hora,fecha,ls,cd,back

from comandos.io.archivo import archivo
from comandos.io.lector import lector

from comandos.programacion.python.npy import npy

from comandos.utileria.git import git

class NekoShell(cmd.Cmd):

    def __init__(self, completekey = "tab", stdin = None, stdout = None):
        super().__init__(completekey, stdin, stdout)
        
        self.version = "1.0.2"
        
        self.rutaRoot = "/"
        self.usu = usuario()
        self.prompt = f"{Fore.GREEN} Neko Shell {self.usu} - {self.rutaRoot} >> {Style.RESET_ALL}"

        self.env = ""
        self.envScripts = ""


    def do_nversion(self,args):
       nversion(self.version)

    def do_nusuario(self,args):
        print(f"{Fore.YELLOW} El usuario activo es {usuario()}")
       

    def do_nusuarios(self,args):
       usuarios()
    
    def do_nlimpiar(self,args):
       limpiar()

    def do_nhora(self,args):
        hora()
        
    
    def do_nfecha(self,args):
        fecha()

        
    def do_narchivo(self,args):
        archivo(args)
        

    def do_nlector(self,args):
        lector(args)
      

    def do_nsalir(self,args):
        return True

    def do_nls(self,args):
        ls(args,self.rutaRoot)

        
    def do_ncd(self, args):
        
        operacion = cd(args,self.rutaRoot)

        valor_error = operacion.get("error")

        if valor_error is not None:

            print(operacion["contenido"])
        else:

            if operacion["base"] == True:
                self.prompt = f"{Fore.GREEN} Neko Shell {usuario()} - {operacion["argumento"]} >> {Style.RESET_ALL}"
                self.rutaRoot = operacion["argumento"]
            else:
                self.prompt = f"{Fore.GREEN} Neko Shell {usuario()} - {operacion["argumento"]} >> {Style.RESET_ALL}"
                self.rutaRoot = operacion["argumento"]
            

    def do_nback(self,args):
        path = back(self.rutaRoot)
        if path == "/" or (len(path) == 3 and ":"in path):
            self.prompt = f"{Fore.GREEN} Neko Shell {usuario()} - {path} >> {Style.RESET_ALL}"
            self.rutaRoot = path 
        else:
            self.prompt = f"{Fore.GREEN} Neko Shell {usuario()} - {path+"/"} >> {Style.RESET_ALL}"
            self.rutaRoot = path + "/" 
    
    def do_npy(self,args):
        
        resultado = npy(self.rutaRoot,self.env,self.envScripts,args)

        if resultado is not None:

            if resultado["proceso"] == "virtual":
                self.prompt = f"{Fore.MAGENTA}(env){Fore.GREEN} Neko Shell {usuario()} - {self.rutaRoot} >> {Style.RESET_ALL}" 
                self.env = resultado["env"]
                self.envScripts = resultado["envScripts"]
        
                
    def do_nreset(self,args):
        self.prompt = f"{Fore.GREEN} Neko Shell {usuario()} - {self.rutaRoot} >> {Style.RESET_ALL}" 
        self.env = False
        self.envScripts = ""  
    
    def do_ngit(self,args):

        git(self.rutaRoot,args)