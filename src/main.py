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
import criptografia.cesar

def inicio():
    os.system("cls")
    banner = header.figlet_format("Cybersecurity Tasks")
    print(colored(banner.rstrip("\n"), "red", attrs=["bold"]))

def selecciona():
    try:

        opcion = 0
        while True:
            opcion = input("[**] Elige una opción > ")
            if not opcion:
                break
            print(colored("[INFO] Seleccionar una opcion del menu", "red", attrs=["bold"]))
    except Exception:
        print(colored("[ERROR] Ha ocurrido un error", "red", attrs=["bold"]))
        print(colored("[ERROR] Introduce un numero entero", "red", attrs=["bold"]))
    return opcion

def main():    
    opcion = 0
    inicio()
    try:
        while True:
            print(colored("[01] Web Scraping", "green", attrs=["bold"]))
            print(colored("[02] Escaneo de Puertos", "green", attrs=["bold"]))
            print(colored("[03] Cifrado de Mensajes", "green", attrs=["bold"]))
            print(colored("[04] Envío de Correos", "green", attrs=["bold"]))
            print(colored("[05] Obtención de Metadatos", "green", attrs=["bold"]))
            print(colored("[06] Salir", 'green', attrs=["bold"]))
            opcion = selecciona()
            if opcion == "1" or opcion == "01":
                print(colored("Web Scraping", "red", attrs=["bold"]))
            elif opcion == "2" or opcion == "02":
                print(colored("Escaneo de Puertos", "red", attrs=["bold"]))
            elif opcion == "3" or opcion == "03":
                print(colored("Cifrado de Mensajes", "red", attrs=["bold"]))
            elif opcion == "4" or opcion == "04":
                print(colored("Envío de Correos", "red", attrs=["bold"]))
            elif opcion == "5" or opcion == "05":
                print(colored("Obtención de Metadatos", "red", attrs=["bold"]))
            elif opcion == "6" or opcion == "06":
                print(colored(str(datetime.now()) + " [INFO] By Andrés Hernández Mata | Versión 1.1.0 | LSTI", "yellow", attrs=["bold"]))
                print(colored(str(datetime.now()) + " [INFO] Gracias", "yellow", attrs=["bold"]))
                break
            else:
                os.system("cls")
                print(colored("[INFO] Por favor, introduce una opcion valida", "red", attrs=["bold"]))
    except Exception as error:
        print(colored("[ERROR] Ha ocurrido un error", "red", attrs=["bold"]))
        print(colored(error, 'red', attrs=['bold']))

if __name__ == "__main__":
    main()
