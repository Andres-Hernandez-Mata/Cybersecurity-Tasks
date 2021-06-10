"""
Uso: Escaneo
Creado: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 09 Junio 2021
"""

import logging
from termcolor import colored
from datetime import datetime
from scanner.check_ports_socket import Puerto

logging.basicConfig(level=logging.INFO, filename="cybersecurity_tasks.log", format="%(asctime)s %(levelname)s:%(message)s")
puerto = Puerto()

class Escanear:

    def escanear(self):
        try:
            while True:
                ip = input("\nTarget > ")
                port_list = input("Puertos > ")
                if not ip or not port_list:
                    print(colored("%s [INFO] El target y el puerto son datos obligatorios" % datetime.now(), "red", attrs=["bold"]))
                else:
                    break
            
            port_list = port_list.split(",")
    
            for i in range(len(port_list)):   
                port_list[i] = int(port_list[i])
    
            puerto.check_ports_socket(ip, port_list)
        
        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}\n".format(error), "red", attrs=["bold"]))



