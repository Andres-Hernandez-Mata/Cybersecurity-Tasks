"""
Uso: Escanear puertos
Creado: Andrés Hernández Mata
Version: 2.5.0
Python: 3.9.1
Fecha: 16 Abril 2021
"""

import os
import pyfiglet as header
import logging
from termcolor import colored
from datetime import datetime
from scanner.scanner_nmap import ScannerNmap
from scanner.escanear import Escanear
from opcion.menu_opcion import Opcion

clear = lambda: os.system("cls" if os.name=="nt" else "clear")
logging.basicConfig(level=logging.INFO, filename="cybersecurity_tasks.log", format="%(asctime)s %(levelname)s:%(message)s")
scanner_nmap = ScannerNmap()
escanear = Escanear()
opcion = Opcion()
global opcion_menu

class ScannerPuertos:

    def menu(self):
        clear()
        banner = header.figlet_format("Scanner")
        print(colored(banner.rstrip("\n"), "red", attrs=["bold"]))        
        try:
            while True:
                print(colored("[01] Socket", "green", attrs=["bold"]))
                print(colored("[02] Nmap", "green", attrs=["bold"]))
                print(colored("[03] Salir", "green", attrs=["bold"]))
                opcion_menu = opcion.opcion()      
                if opcion_menu == "1" or opcion_menu == "01":
                    escanear.escanear()
                elif opcion_menu == "2" or opcion_menu == "02":                    
                    scanner_nmap.scanner_nmap()
                elif opcion_menu == "3" or opcion_menu == "03":
                    clear()
                    break
                else:                    
                    print(colored("%s [INFO] Introduce una opcion valida del menú \n" % datetime.now(), "red", attrs=["bold"]))
        
        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}\n".format(error), "red", attrs=["bold"]))

