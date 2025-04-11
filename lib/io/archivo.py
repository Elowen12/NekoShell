from pynput import keyboard
from colorama import Fore, Style, init

class Archivo:

    def __init__(self,nombre):
        self.nombre = nombre
        self.escribiendo = True

    def escribir(self):

        try:
            
            print("hola")
            with open(self.nombre, "wt+") as arch:
                print("Puede empezar a escribir, para salir presione 'Esc'")

                def on_press(key):
                    try:
                        if key == keyboard.Key.esc:  # Detectar tecla 'Esc'
                            print("Guardando documento...")
                            self.escribiendo = False
                            return False  # Detener el listener
                    except Exception as e:
                        print(f"Error detectando tecla: {e}")

                # Inicia el listener para capturar eventos de teclado
                with keyboard.Listener(on_press=on_press) as listener:
                    while self.escribiendo:
                        texto = input(f"{Fore.BLUE}>> ")  # Permitir al usuario escribir
                        arch.write(texto + "\n")
        except:
            print("No se puedo generar el archivo.")
