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
from scanner.check_ports_socket import Puerto

clear = lambda: os.system("cls" if os.name=="nt" else "clear")
logging.basicConfig(level=logging.INFO, filename="cybersecurity_tasks.log", format="%(asctime)s %(levelname)s:%(message)s")

class Escaneo:

    def escanear(self):
        try:
            while True:
                ip = input("\nTarget > ")
                port_list = input("Puertos > ")
                if not ip or not port_list:
                    print(colored("%s [INFO] El target y el puerto son datos obligatorios \n" % datetime.now(), "red", attrs=["bold"]))
                else:
                    break
            
            port_list = port_list.split(",")
    
            for i in range(len(port_list)):        
                port_list[i] = int(port_list[i])
    
            puerto = Puerto()
            puerto.check_ports_socket(ip, port_list)   
        
        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}\n".format(error), "red", attrs=["bold"]))        

    def option(self):
        try:            
            while True:
                opcion = input("[**] Elige una opción > ")
                if opcion:                
                    break
                print(colored("\n%s [INFO] Seleccionar una opción del menú" % datetime.now(), "red", attrs=["bold"]))
        
        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))   
            print(colored("{}\n".format(error), "red", attrs=["bold"]))
        
        return opcion

    def menu(self):
        clear()
        banner = header.figlet_format("Scanner")
        print(colored(banner.rstrip("\n"), "red", attrs=["bold"]))        
        try:
            while True:
                print(colored("[01] Escanear puerto con socket", "green", attrs=["bold"]))
                print(colored("[02] Salir", "green", attrs=["bold"]))
                opcion = str()
                escaneo = Escaneo()
                opcion = escaneo.option()
                if opcion == "1" or opcion == "01":
                    escaneo.escanear()
                elif opcion == "2" or opcion == "02":
                    clear()
                    break
                else:                    
                    print(colored("\n%s [INFO] Introduce una opcion valida del menú" % datetime.now(), "red", attrs=["bold"]))
        
        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored(error, "red", attrs=["bold"]))

