"""
Uso: API
Creador: Andrés Hernández Mata
Version: 3.5.0
Python: 3.8.5
Fecha: 19 Mayo 2021
"""

import shodan
import logging
from datetime import datetime
from termcolor import colored

logging.basicConfig(level=logging.INFO, filename="cybersecurity_tasks.log", format="%(asctime)s %(levelname)s:%(message)s")

class Conectar:

    def key(self):
        try:
            while True:
                key = input("\nAPI Key > ")
                if not key:
                    print(colored("%s [INFO] La API Key es un dato obligatorio" % datetime.now(), "red", attrs=["bold"]))
                else:
                    break
            
        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}\n".format(error), "red", attrs=["bold"]))
        
        return key
    
    def buscar(self):
        try:
            while True:
                buscar = input("Buscar > ")
                if not buscar:
                    print(colored("%s [INFO] La busqueda es un dato obligatorio \n" % datetime.now(), "red", attrs=["bold"]))
                else:
                    break

        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}\n".format(error), "red", attrs=["bold"]))
        
        return buscar
    
    def conectar(self):
        try:
            conectar = Conectar()
            key = conectar.key()
            api = shodan.Shodan(key)
            buscar = conectar.buscar()
            results = api.search(buscar, limit=5)
            print(colored("{} [INFO] Resultados: {}".format(datetime.now(), results["total"]), "green", attrs=["bold"]))
            for result in results["matches"]:
                print(colored("{} [INFO] IP: {}".format(datetime.now(), result["ip_str"]), "green", attrs=["bold"]))
                print("{}\n".format(result["data"]))
        
        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}\n".format(error), "red", attrs=["bold"]))

