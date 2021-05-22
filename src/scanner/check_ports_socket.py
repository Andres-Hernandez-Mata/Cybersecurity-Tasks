"""
Uso: Socket
Creado: Andrés Hernández Mata
Version: 2.5.0
Python: 3.9.1
Fecha: 16 Abril 2021
"""

import socket
import logging
from termcolor import colored
from datetime import datetime

logging.basicConfig(level=logging.INFO, filename="cybersecurity_tasks.log", format="%(asctime)s %(levelname)s:%(message)s")
class Puerto:
    
    def check_ports_socket(self, ip, portlist):
        try:
            print("----------------------------------------------------------")
            for port in portlist:
                sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                result = sock.connect_ex((ip, port))                
                if result == 0:
                    print(colored("{} [INFO] Puerto {}:\tAbierto".format(datetime.now(), port), "green", attrs=["bold"]))
                else:
                    print(colored("{} [INFO] Puerto {}:\tCerrado".format(datetime.now(), port), "green", attrs=["bold"]))
            print("----------------------------------------------------------\n")
        except socket.error as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}\n".format(error), "red", attrs=["bold"]))            
        finally:
            sock.close()


