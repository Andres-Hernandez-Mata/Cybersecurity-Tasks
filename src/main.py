"""
Uso: Menú principal
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.8.5
Fecha: 05 Marzo 2021
"""

import os
from colorama import Fore
from colorama import Style
import pyfiglet as header
from termcolor import colored

os.system("cls")

def inicio():
    banner = header.figlet_format("Cybersecurity Tasks")
    print(colored(banner.rstrip("\n"), "red", attrs=["bold"]))
    print(colored("         By Andrés Hernández Mata | Versión 1.0.0 | LSTI \n", "yellow", attrs=["bold"]))

def selecciona():
    try:        
        opcion = 0
        while True:
            opcion = input("[**] Elige una opción > ")
            break
    except Exception:
        print(colored("Error, introduce un numero entero", "red", attrs=["bold"]))
    return opcion

def menu():    
    opcion = 0
    try:
        while True:
            print(colored("[01] Web Scraping", "green", attrs=["bold"]))
            print(colored("[02] Escaneo de Puertos", "green", attrs=["bold"]))
            print(colored("[03] Cifrado de Mensajes", "green", attrs=["bold"]))
            print(colored("[04] Envío de Correos", "green", attrs=["bold"]))
            print(colored("[05] Obtención de Metadatos", "green", attrs=["bold"]))
            print(colored("[06] Salir", 'red', attrs=["bold"]))
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
                print(colored("[INFO] Adios", "yellow", attrs=["bold"]))
                break                
            else:
                os.system("cls")
                print(colored("Por favor, introduce una opcion valida", "red", attrs=["bold"]))
    except Exception as error:
        print(colored(error, 'red', attrs=['bold']))

if __name__ == "__main__":
    inicio()
    menu()
    

