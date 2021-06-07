"""
Uso: Scapy Dot11
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.8.5
Fecha: 21 Mayo 2021
"""

import os
import logging
import pyfiglet as header
from datetime import datetime
from termcolor import colored
from scapydot11.network import Network
from opcion.menu_opcion import Opcion

clear = lambda: os.system("cls" if os.name=="nt" else "clear")
logging.basicConfig(level=logging.INFO, filename="cybersecurity_tasks.log", format="%(asctime)s %(levelname)s:%(message)s")
network = Network()
opcion = Opcion()
global opcion_menu

class ScapyDot11:
    
    def menu(self):
        clear()
        banner = header.figlet_format("Scapy Dot11")
        print(colored(banner.rstrip("\n"), "red", attrs=["bold"]))
        try:
            while True:                
                print(colored("[01] MAC address", "green", attrs=["bold"]))
                print(colored("[02] Salir", "green", attrs=["bold"]))
                opcion_menu = opcion.opcion()
                if opcion_menu == "1" or opcion_menu == "01":                   
                   network.mac_address()
                elif opcion_menu == "2" or opcion_menu == "02":
                    clear()
                    break
                else:                    
                    print(colored("%s [INFO] Introduce una opción valida del menú \n" % datetime.now(), "red", attrs=["bold"]))
        
        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}\n".format(error), "red", attrs=["bold"]))