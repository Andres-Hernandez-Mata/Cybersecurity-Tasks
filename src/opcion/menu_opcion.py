"""
Uso: Opcion
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 02 Junio 2021
"""

import logging
from termcolor import colored
from datetime import datetime

logging.basicConfig(level=logging.INFO, filename="cybersecurity_tasks.log", format="%(asctime)s %(levelname)s:%(message)s")

class Opcion:
    
    def opcion(self):
        try:
            i = True
            while(i == True):
                opcion = input("[**] Elige una opción > ")
                if not opcion:
                    print(colored("{} [INFO] Seleccionar una opción del menú \n".format(datetime.now()), "red", attrs=["bold"]))
                else:
                    i = False                                    

        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}\n".format(error), "red", attrs=["bold"]))

        return opcion