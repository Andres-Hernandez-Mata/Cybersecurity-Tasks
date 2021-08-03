"""
Uso: Menu hash
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.8.5
Fecha: 22 Mayo 2021
"""

import os
import pyfiglet as header
import logging
from datetime import datetime
from termcolor import colored
from hash.sha512 import Sha512
from opcion.menu_opcion import Opcion

clear = lambda: os.system("cls" if os.name=="nt" else "clear")
logging.basicConfig(level=logging.INFO, filename="cybersecurity_tasks.log", format="%(asctime)s %(levelname)s:%(message)s")
opcion = Opcion()
sha512 = Sha512()
global opcion_menu

class Hash:
    
    def menu(self):
        clear()
        banner = header.figlet_format("Hash SHA512")
        print(colored(banner.rstrip("\n"), "red", attrs=["bold"]))
        try:
            while True:                
                print(colored("[01] SHA512", "green", attrs=["bold"]))
                print(colored("[02] Salir", "green", attrs=["bold"]))                                
                opcion_menu = opcion.opcion()
                if opcion_menu == "1" or opcion_menu == "01":                   
                   sha512.hash_sha512()
                elif opcion_menu == "2" or opcion_menu == "02":
                    clear()
                    break
                else:                    
                    print(colored("%s [INFO] Introduce una opción valida del menú \n" % datetime.now(), "red", attrs=["bold"]))
        
        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored(error, "red", attrs=["bold"]))
