from lib.io.lector import Lector
from colorama import Fore, Style, init

def lector(args):

    argumentos = args.split()

    if len(argumentos) > 0:
            
        try:

            lector = Lector(argumentos[0])

            texto = lector.leer()

            print(f"{Fore.BLUE}{texto}")
            
        except:
            print("No se pudo leer el archivo solicitado.")