"""
Uso: Menu de metadata
Creador: Andrés Hernández Mata
Version: 1.4.0
Python: 3.9.1
Fecha: 16 Mayo 2021
"""

import os
import pyfiglet as header
from termcolor import colored
from datetime import datetime
from metadata.extract_data_images import Imagenes
from metadata.extract_data_pdf import Documentos

clear = lambda: os.system("cls" if os.name=="nt" else "clear")

class Metadata:

    def option(self):
        try:            
            while True:
                opcion = input("[**] Elige una opción > ")
                if not opcion:
                    print(colored("\n%s [INFO] Seleccionar una opción del menú" % datetime.now(), "red", attrs=["bold"]))
                else:
                    break                
        
        except Exception as error:
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))   
            print(colored("{}\n".format(error), "red", attrs=["bold"]))
        
        return opcion

    def menu(self):
        clear()
        banner = header.figlet_format("Metadata")
        print(colored(banner.rstrip("\n"), "red", attrs=["bold"]))        
        try:
            while True:                
                print(colored("[01] Extraer metadata de imagenes", "green", attrs=["bold"]))
                print(colored("[02] Extraer metadata de PDF's", "green", attrs=["bold"]))
                print(colored("[03] Salir", "green", attrs=["bold"]))
                opcion = str()
                metadata = Metadata()
                imagenes = Imagenes()
                documentos = Documentos()
                opcion = metadata.option()
                if opcion == "1" or opcion == "01":                    
                    imagenes.get_metadata_imagenes()
                elif opcion == "2" or opcion == "02":                    
                    documentos.get_metadata_pdf()
                elif opcion == "3" or opcion == "03":
                    clear()
                    break
                else:                  
                    print(colored("\n%s [INFO] Introduce una opción valida del menú" % datetime.now(), "red", attrs=["bold"]))
        
        except Exception as error:
            print(colored("\n%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored(error, "red", attrs=["bold"]))

