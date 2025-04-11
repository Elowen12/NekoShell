from colorama import Fore, Style, init
from lib.sistema.usuario import Usuarios

def usuario():
    usu = Usuarios()
    return usu.Activo()

def usuarios():
    usu = Usuarios()
    usu.listaUsuarios()