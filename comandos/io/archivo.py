from lib.utileria.validaciones import validarNombreArchivo
from lib.io.archivo import Archivo

def archivo(args):

    argumentos = args.split()

    if len(argumentos) == 1:

        nombreArchivo = validarNombreArchivo(argumentos[0])

        if nombreArchivo:
            archivo = Archivo(argumentos[0])
            archivo.escribir()
    
    else:
        print("Debes asignarle un nombre al archivo ejemplo: documento.txt")