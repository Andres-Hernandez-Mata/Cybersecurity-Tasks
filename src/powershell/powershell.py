"""
Uso: Menú PowerShell
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.8.5
Fecha: 21 Mayo 2021
"""

import os
import pyfiglet as header
import logging
from datetime import datetime
from termcolor import colored
from powershell.shell import Shell

clear = lambda: os.system("cls" if os.name=="nt" else "clear")
logging.basicConfig(level=logging.INFO, filename="cybersecurity_tasks.log", format="%(asctime)s %(levelname)s:%(message)s")

class PowerShell:
    
    def option(self):
        try:
            while True:
                opcion = input("[**] Elige una opción > ")
                if not opcion:
                    print(colored("%s [INFO] Seleccionar una opción del menú \n" % datetime.now(), "red", attrs=["bold"]))
                else:
                    break    
        
        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("%s [ERROR] Introduce un numero entero" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}\n".format(error), "red", attrs=["bold"]))
        
        return opcion
    
    def menu(self):
        clear()
        banner = header.figlet_format("PowerShell")
        print(colored(banner.rstrip("\n"), "red", attrs=["bold"]))
        try:
            while True:                
                print(colored("[01] Comando", "green", attrs=["bold"]))
                print(colored("[02] Salir", "green", attrs=["bold"]))
                opcion = str()
                powerShell = PowerShell()
                opcion = powerShell.option()
                if opcion == "1" or opcion == "01":
                    shell = Shell()
                    shell.ejecutar()                    
                elif opcion == "2" or opcion == "02":
                    clear()
                    break
                else:                    
                    print(colored("%s [INFO] Introduce una opción valida del menú \n" % datetime.now(), "red", attrs=["bold"]))
        
        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored(error, "red", attrs=["bold"]))

