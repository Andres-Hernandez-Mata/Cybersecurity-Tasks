"""
Uso: Shell
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.8.5
Fecha: 21 Mayo 2021
"""

import subprocess
import logging
from datetime import datetime
from termcolor import colored

logging.basicConfig(level=logging.INFO, filename="cybersecurity_tasks.log", format="%(asctime)s %(levelname)s:%(message)s")

class Shell:   

    def comando(self):
        try:
            while True:
                comando = input("\n> ")                
                if not comando:
                    print(colored("%s [INFO] El comando es un dato obligatorio" % datetime.now(), "red", attrs=["bold"]))
                else:
                    break

        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}\n".format(error), "red", attrs=["bold"]))
    
        return comando
    
    def ejecutar(self):
        try:
            shell = Shell()
            comando = shell.comando()            
            lineaPS = 'powershell -Executionpolicy ByPass -File powershell/comando.ps1 -comando "{}"'.format(comando)
            runningProcesses = subprocess.check_output(lineaPS)
            print(colored("\n{} [INFO] {}".format(datetime.now(), comando), "green", attrs=["bold"]))       
            print(colored(runningProcesses.decode("utf-8", "ignore"), "yellow", attrs=["bold"]))
        
        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}\n".format(error), "red", attrs=["bold"]))


