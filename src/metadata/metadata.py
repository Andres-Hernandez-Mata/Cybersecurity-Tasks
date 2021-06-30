"""
Uso: Menu de metadata
Creador: Andrés Hernández Mata
Version: 2.0.0
Python: 3.9.1
Fecha: 16 Mayo 2021
"""

import os
import pyfiglet as header
import logging
from termcolor import colored
from datetime import datetime
from metadata.extract_data_images import Imagenes
from metadata.extract_data_pdf import Documentos
from opcion.menu_opcion import Opcion

clear = lambda: os.system("cls" if os.name=="nt" else "clear")
logging.basicConfig(level=logging.INFO, filename="cybersecurity_tasks.log", format="%(asctime)s %(levelname)s:%(message)s")
opcion = Opcion()
imagenes = Imagenes()
documentos = Documentos()
global opcion_menu

class Metadata:

    def menu(self):
        clear()
        banner = header.figlet_format("Metadata")
        print(colored(banner.rstrip("\n"), "red", attrs=["bold"]))        
        try:
            while True:                
                print(colored("[01] Extraer metadata de imagenes", "green", attrs=["bold"]))
                print(colored("[02] Extraer metadata de PDF's", "green", attrs=["bold"]))
                print(colored("[03] Salir", "green", attrs=["bold"]))
                opcion_menu = opcion.opcion()
                if opcion_menu == "1" or opcion_menu == "01":                    
                    imagenes.get_metadata_imagenes()
                elif opcion_menu == "2" or opcion_menu == "02":                    
                    documentos.get_metadata_pdf()
                elif opcion_menu == "3" or opcion_menu == "03":
                    clear()
                    break
                else:                  
                    print(colored("%s [INFO] Introduce una opción valida del menú" % datetime.now(), "red", attrs=["bold"]))
        
        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("\n%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored(error, "red", attrs=["bold"]))

