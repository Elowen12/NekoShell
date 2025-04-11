import os

class Class:

    def __init__(self,ruta,nombre):
        self.ruta = ruta
        self.clase = nombre
    
    def crear(self):

        try:

            with open(self.ruta,"wt+") as archivo:
                archivo.write(f"#Clase {self.clase}"+"\n")
                archivo.write(f"class {self.clase}:"+"\n")
                archivo.write(f"    def __init__():"+"\n")
                archivo.write(f"        pass"+"\n")
                archivo.write(f"    def funcion():"+"\n")
                archivo.write(f"        pass"+"\n")
        
            return True
        
        except:

            return False

