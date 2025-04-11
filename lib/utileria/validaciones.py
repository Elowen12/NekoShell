import re
import os

def validarNombreArchivo(nombre):
    # Definir el patrón para la validación
    patron = r'^[a-zA-Z0-9._-]+\.[a-zA-Z0-9]+$'
    
    # Validar el nombre del archivo
    if re.match(patron, nombre):
        return True
    else:
        return False

def validarRuta(nombre):
    # Definir el patrón para la validación
    patron = r'^[a-zA-Z0-9._/:-]+$'
    
    # Validar el nombre del archivo
    if re.match(patron, nombre):
        return True
    else:
        return False
    
def validarNombre(nombre):
    
    # Expresión regular para validar números, letras, "_" y "-"
    patron = r'^[a-zA-Z0-9_-]+$'
    return bool(re.match(patron, nombre))

def validarTexto(texto):
    patron = r'^[a-zA-Z0-9._\-"\'\s]+$'
    if re.match(patron, texto):
        return True  # Cadena válida
    else:
        return False  # Cadena inválida


    
