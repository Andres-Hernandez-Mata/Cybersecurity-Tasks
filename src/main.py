"""
Uso: Menú principal
Creador: Andrés Hernández Mata
Version: 5.0.0
Python: 3.9.1
Fecha: 05 Marzo 2021
"""

import os
import pyfiglet as header
import argparse
import logging
from termcolor import colored
from datetime import datetime
from cifrado.cesar import Cesar
from correo.send_email import Correo
from scanner.scanner_puertos import ScannerPuertos
from metadata.metadata import Metadata
from scraping.beautiful_soup import Beautiful
from scraping.scraping import Scraping
from api.shodan import Shodan
from powershell.powershell import PowerShell
from scapydot11.scapy_dot11 import ScapyDot11
from hash.hash import Hash
from opcion.menu_opcion import Opcion

clear = lambda: os.system("cls" if os.name=="nt" else "clear")
logging.basicConfig(level=logging.INFO, filename="cybersecurity_tasks.log", format="%(asctime)s %(levelname)s:%(message)s")
opcion = Opcion()
global opcion_menu

def arg():
    try:
        descripion = "example: -url https://www.google.com.mx"
        parser = argparse.ArgumentParser(description="Cybersecurity Tasks [01] Web Scraping", epilog=descripion, formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument("-url,", metavar='--url', dest="url", help="URL para hacer web scraping", required=False)
        params = parser.parse_args()
        url = params.url
        if url:
            scraping = Scraping()
            scraping.requests_get(url)
            quit()

    except Exception as error:
        logging.error(error, exc_info=True)
        print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
        print(colored("{}\n".format(error), "red", attrs=["bold"]))

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
            print(colored("[06] API de Shodan", "green", attrs=["bold"]))
            print(colored("[07] Uso de Windows PowerShell", "green", attrs=["bold"]))
            print(colored("[08] Scapy Dot11", "green", attrs=["bold"]))
            print(colored("[09] Hash SHA512", "green", attrs=["bold"]))
            print(colored("[10] Salir", "green", attrs=["bold"]))
            opcion_menu = opcion.opcion()
            if opcion_menu == "1" or opcion_menu == "01":
                print(colored("%s Web Scraping" % datetime.now(), "green", attrs=["bold"]))
                beautiful = Beautiful()
                beautiful.menu()
            elif opcion_menu == "2" or opcion_menu == "02":
                print(colored("%s Escaneo de Puertos" % datetime.now(), "green", attrs=["bold"]))
                scanner_puertos = ScannerPuertos()
                scanner_puertos.menu()
            elif opcion_menu == "3" or opcion_menu == "03":
                print(colored("%s Cifrado de Mensajes" % datetime.now(), "green", attrs=["bold"]))
                cesar = Cesar()
                cesar.menu()
            elif opcion_menu == "4" or opcion_menu == "04":
                print(colored("%s Envío de Correos" % datetime.now(), "green", attrs=["bold"]))
                correo = Correo()
                correo.menu()
            elif opcion_menu == "5" or opcion_menu == "05":
                print(colored("%s Obtención de Metadatos" % datetime.now(), "green", attrs=["bold"]))
                metadata = Metadata()
                metadata.menu()
            elif opcion_menu == "6" or opcion_menu == "06":
                print(colored("%s API de Shodan" % datetime.now(), "green", attrs=["bold"]))
                shodan = Shodan()
                shodan.menu()
            elif opcion_menu == "7" or opcion_menu == "07":
                print(colored("%s Uso de Windows PowerShell" % datetime.now(), "green", attrs=["bold"]))
                powershell = PowerShell()
                powershell.menu()
            elif opcion_menu == "8" or opcion_menu == "08":
                print(colored("%s Scapy Dot11" % datetime.now(), "green", attrs=["bold"]))
                scapy_dot = ScapyDot11()
                scapy_dot.menu()
            elif opcion_menu == "9" or opcion_menu == "09":
                print(colored("%s Hash SHA512" % datetime.now(), "green", attrs=["bold"]))
                hash = Hash()
                hash.menu()
            elif opcion_menu == "10":
                print(colored("\n%s [INFO] By Andrés Hernández Mata | Versión 5.0.0 | LSTI" % datetime.now(), "green", attrs=["bold"]))
                print(colored("%s [INFO] Gracias \n" % datetime.now(), "green", attrs=["bold"]))
                break
            else:
                print(colored("%s [INFO] Por favor, introduce una opción valida" % datetime.now(), "red", attrs=["bold"]))

    except Exception as error:
        logging.error(error, exc_info=True)
        print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
        print(colored(error, "red", attrs=["bold"]))
    except KeyboardInterrupt:
        quit()

if __name__ == "__main__":
    main()
