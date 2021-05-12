"""
Uso: Menú principal
Creador: Andrés Hernández Mata
Version: 1.2.0
Python: 3.8.5
Fecha: 05 Marzo 2021
"""

import os
from colorama import Fore
from colorama import Style
import pyfiglet as header
from termcolor import colored
from datetime import datetime
from criptografia.cesar import Cesar

clear = lambda: os.system("cls" if os.name=="nt" else "clear")

def option():
    try:
        while True:
            opcion = input("[**] Elige una opción > ")
            if opcion:                
                break
            print(colored("[INFO] Seleccionar una opcion del menu", "red", attrs=["bold"]))
    
    except Exception:
        print(colored("[ERROR] Ha ocurrido un error", "red", attrs=["bold"]))
        print(colored("[ERROR] Introduce un numero entero", "red", attrs=["bold"]))
    return opcion

def main():
    try:
        while True:
            print(colored("[01] Web Scraping", "green", attrs=["bold"]))
            print(colored("[02] Escaneo de Puertos", "green", attrs=["bold"]))
            print(colored("[03] Cifrado de Mensajes", "green", attrs=["bold"]))
            print(colored("[04] Envío de Correos", "green", attrs=["bold"]))
            print(colored("[05] Obtención de Metadatos", "green", attrs=["bold"]))
            print(colored("[06] Salir", "green", attrs=["bold"]))
            opcion = option()
            if opcion == "1" or opcion == "01":
                print(colored("%s Web Scraping" % datetime.now(), "red", attrs=["bold"]))
            elif opcion == "2" or opcion == "02":
                print(colored("%s Escaneo de Puertos" % datetime.now(), "red", attrs=["bold"]))
            elif opcion == "3" or opcion == "03":
                print(colored("%s Cifrado de Mensajes" % datetime.now(), "red", attrs=["bold"]))
            elif opcion == "4" or opcion == "04":
                print(colored("%s Envío de Correos" % datetime.now(), "red", attrs=["bold"]))
            elif opcion == "5" or opcion == "05":
                print(colored("%s Obtención de Metadatos" % datetime.now(), "red", attrs=["bold"]))
            elif opcion == "6" or opcion == "06":
                print(colored("%s [INFO] By Andrés Hernández Mata | Versión 1.2.0 | LSTI" % datetime.now(), "blue", attrs=["bold"]))
                print(colored("%s [INFO] Gracias" % datetime.now(), "blue", attrs=["bold"]))
                break
            else:
                print(colored("%s [INFO] Por favor, introduce una opcion valida" % datetime.now(), "red", attrs=["bold"]))
    
    except Exception as error:
        print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
        print(colored(error, "red", attrs=["bold"]))
    except KeyboardInterrupt:
        quit()

if __name__ == "__main__":    
    clear()
    banner = header.figlet_format("Cybersecurity Tasks")
    print(colored(banner.rstrip("\n"), "red", attrs=["bold"]))
    main()
