import os
import wmi
from colorama import Fore, Style, init

class Usuarios:

    def Activo(self):
        return os.getlogin()
    
    def listaUsuarios(self):
        i = 1
        c = wmi.WMI()
        
        usuarios = c.Win32_UserAccount()

        for usuario in usuarios:
            print(f"{Fore.YELLOW} Usuario: {usuario.Name}")
            grupos_usuario = c.Win32_GroupUser(PartComponent=f'Win32_UserAccount.Domain="{usuario.Domain}",Name="{usuario.Name}"')
            if grupos_usuario:
                print(f"{Fore.YELLOW}Grupos:")
                for grupo in grupos_usuario:
                    try:
                        # Verificar contenido de GroupComponent antes de manipularlo
                        group_component = grupo.GroupComponent
                        
                        print(f"{Fore.WHITE}{group_component.Domain}")
                        print(f"{Fore.WHITE}{group_component.Name}")
                        if group_component.LocalAccount:
                            print(f"{Fore.WHITE}Cuenta local")
                        else:
                            print(f"{Fore.WHITE}Cuenta externa")
                        print(f"{Fore.WHITE}{group_component.Description}")
                        print(f"{Fore.WHITE}-----------------------------")
                        
                    except Exception as inner_e:
                        print(f"{Fore.WHITE}No se pudo analizar los grupos a los que pertenece")

            else:
                print(f"{Fore.WHITE}No pertenece a ningún grupo.")