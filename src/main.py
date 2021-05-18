"""
Uso: Menú principal
Creador: Andrés Hernández Mata
Version: 3.0.0
Python: 3.8.5
Fecha: 05 Marzo 2021
"""

import os
import pyfiglet as header
import argparse
from termcolor import colored
from datetime import datetime
from cifrado.cesar import Cesar
from correo.send_email import Correo
from scanner.scanner_puertos import Escaneo
from metadata.metadata import Metadata
from scraping.beautiful_soup import Beautiful
from scraping.scraping import Scraping

clear = lambda: os.system("cls" if os.name=="nt" else "clear")

def arg():
    try:
        descripion = "example: -url https://www.google.com.mx"
        parser = argparse.ArgumentParser(description="Cybersecurity Tasks [01] Web Scraping", epilog=descripion, formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument("-url,", metavar='--url', dest="url", help="URL para hacer web scraping", required=False)
        params = parser.parse_args()
        url = params.url
        if url:
            scraping = Scraping()
            scraping.scraping_beautiful_soup(url)
            scraping.scraping_pdf(url)
            scraping.scraping_links(url)
            quit()

    except Exception as error:
        print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))   
        print(colored("{}\n".format(error), "red", attrs=["bold"]))    

def option():
    try:
        while True:
            opcion = input("[**] Elige una opción > ")
            if opcion:  
                break
            print(colored("\n%s [INFO] Seleccionar una opción del menú" % datetime.now(), "red", attrs=["bold"]))
    
    except Exception as error:
        print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))   
        print(colored("{}\n".format(error), "red", attrs=["bold"]))
    
    return opcion

def main():
    try:
        arg()          
        while True:
            clear()
            banner = header.figlet_format("Cybersecurity Tasks")
            print(colored(banner.rstrip("\n"), "red", attrs=["bold"]))
            print(colored("[01] Web Scraping", "green", attrs=["bold"]))
            print(colored("[02] Escaneo de Puertos", "green", attrs=["bold"]))
            print(colored("[03] Cifrado de Mensajes", "green", attrs=["bold"]))
            print(colored("[04] Envío de Correos", "green", attrs=["bold"]))
            print(colored("[05] Obtención de Metadatos", "green", attrs=["bold"]))
            print(colored("[06] Salir", "green", attrs=["bold"]))
            opcion = str()
            opcion = option()            
            if opcion == "1" or opcion == "01":
                print(colored("%s Web Scraping" % datetime.now(), "red", attrs=["bold"]))
                beautiful = Beautiful()
                beautiful.menu()
            elif opcion == "2" or opcion == "02":
                print(colored("%s Escaneo de Puertos" % datetime.now(), "red", attrs=["bold"]))
                escaneo = Escaneo()
                escaneo.menu()
            elif opcion == "3" or opcion == "03":                
                print(colored("%s Cifrado de Mensajes" % datetime.now(), "red", attrs=["bold"]))
                cesar = Cesar()
                cesar.menu()                
            elif opcion == "4" or opcion == "04": 
                print(colored("%s Envío de Correos" % datetime.now(), "green", attrs=["bold"]))
                correo = Correo()
                correo.menu()
            elif opcion == "5" or opcion == "05":
                print(colored("%s Obtención de Metadatos" % datetime.now(), "red", attrs=["bold"]))
                metadata = Metadata()
                metadata.menu()
            elif opcion == "6" or opcion == "06":
                print(colored("\n%s [INFO] By Andrés Hernández Mata | Versión 3.0.0 | LSTI" % datetime.now(), "blue", attrs=["bold"]))
                print(colored("%s [INFO] Gracias" % datetime.now(), "blue", attrs=["bold"]))
                break
            else:
                print(colored("%s [INFO] Por favor, introduce una opción valida" % datetime.now(), "red", attrs=["bold"]))
    
    except Exception as error:        
        print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
        print(colored(error, "red", attrs=["bold"]))        
    except KeyboardInterrupt:
        quit()

if __name__ == "__main__":        
    main()
