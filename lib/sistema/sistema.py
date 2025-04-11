from datetime import datetime
import os

class SO:

    def __init__(self):
        pass

    def hora(self):

        hora_actual = datetime.now()
    
        return hora_actual.strftime("%H:%M:%S")
    
    def fecha(self):

        # Obtener la fecha actual
        fecha_actual = datetime.now()

        # Formatear la fecha en el formato deseado
        fecha_formateada = fecha_actual.strftime("%d/%m/%Y")

        return fecha_formateada
    
    def ls(self,ruta):

        contenido = os.listdir(ruta)

        return contenido
