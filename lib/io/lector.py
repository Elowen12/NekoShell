
class Lector:

    def __init__(self,ruta):
        self.ruta = ruta
    
    def leer(self):

        with open(self.ruta,"r") as archivo:

            return archivo.read()