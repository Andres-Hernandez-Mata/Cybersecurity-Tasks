"""
Uso: Hash
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.8.5
Fecha: 22 Mayo 2021
"""

import hashlib
import os
import logging
import pathlib
from datetime import datetime
from termcolor import colored

logging.basicConfig(level=logging.INFO, filename="cybersecurity_tasks.log", format="%(asctime)s %(levelname)s:%(message)s")

class Sha512:
    
    def directorio(self):
        try:
            while True:
                ruta = input("\nRuta del directorio > ")
                pathRuta = pathlib.Path(ruta)
                if not ruta:
                    print(colored("%s [INFO] La ruta del directorio es un dato obligatorio" % datetime.now(), "red", attrs=["bold"]))
                elif not pathRuta.exists():
                    print(colored("%s [INFO] La ruta del directorio ingresada no existe en el sistema " % datetime.now(), "red", attrs=["bold"]))
                else:
                    break
        
        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}\n".format(error), "red", attrs=["bold"]))
        
        return ruta
    
    def hash_sha512(self):        
        try:
            sha512 = Sha512()
            ruta = sha512.directorio()
            for archivo in os.listdir(ruta):
                if os.path.isfile(archivo):
                    file_obj = open(os.path.join(ruta,archivo),"rb")
                    file = file_obj.read()
                    hash_file = hashlib.sha512(file)
                    hashed_file = hash_file.hexdigest()
                    print(colored("{} [INFO] File > {} ".format(datetime.now(), archivo), "yellow", attrs=["bold"]))
                    print(colored("{} [INFO] SHA512 > {} ".format(datetime.now(), hashed_file), "green", attrs=["bold"]))
            print()
        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}\n".format(error), "red", attrs=["bold"]))