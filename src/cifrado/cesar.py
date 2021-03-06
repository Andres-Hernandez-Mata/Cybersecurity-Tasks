"""
Uso: Cifrado César
Creado: Andrés Hernández Mata
Version: 3.0.0
Python: 3.9.1
Fecha: 10 Mayo 2021
"""

import os
import pyfiglet as header
import logging
from datetime import datetime
from termcolor import colored
from cifrado.spanish import Spanish

clear = lambda: os.system("cls" if os.name=="nt" else "clear")
logging.basicConfig(level=logging.INFO, filename="cybersecurity_tasks.log", format="%(asctime)s %(levelname)s:%(message)s")
class Cesar: 
    
    def cesar(self, mensaje, modo, clave):               
        try:            
        
            simbolos = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
            resultado = ""
                
            for simbolo in mensaje:
                if simbolo in simbolos:
                    indice_simbolo = simbolos.find(simbolo)
                    # Encriptar
                    if modo:                        
                        indice_nuevo = indice_simbolo + int(clave)
                    # Desencriptar
                    elif not modo:                        
                        indice_nuevo = indice_simbolo - int(clave)

                    if indice_nuevo >= len(simbolos):
                        indice_nuevo = indice_nuevo - len(simbolos)
                    elif indice_nuevo < 0:
                        indice_nuevo = indice_nuevo + len(simbolos)
                    resultado = resultado + simbolos[indice_nuevo]
                else:
                    resultado = resultado + simbolo    
        
        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored(error, "red", attrs=["bold"]))        
        
        return resultado, mensaje

    def hackear(self):        
        try:
            while True:            
                mensaje = input("\nMensaje > ")                
                if mensaje:
                    break
                print(colored("%s [INFO] El mensaje es un dato obligatorio" % datetime.now(), "red", attrs=["bold"]))        
        
            cifrado = Cesar()
            for clave in range(1, len(mensaje)):    
                resultado, mensaje = cifrado.cesar(mensaje, False, clave)
                print(colored("%s [INFO] Clave #%s %s" % (datetime.now(), clave, resultado), "green", attrs=["bold"]))

                detect_spanish = Spanish()
                if detect_spanish.spanish(resultado):
                    print()
                    print("Posible mensaje descifrado: ")
                    print("Clave %s: %s" % (clave, resultado[:100]))
                    print()
                    print("¿Si?")
                    response = input("> ")
                    print()

                    if response.strip().upper().startswith("SI"):
                        return resultado, mensaje

        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored(error, "red", attrs=["bold"]))        

        return None, None
    
    def datos(self):
        try:
            while True:            
                mensaje = input("\nMensaje > ")
                clave = int(input("Clave > "))
                if not mensaje and not clave:
                    print(colored("%s [INFO] El mensaje y clave son datos obligatorios" % datetime.now(), "red", attrs=["bold"]))
                else:
                    break                
        
        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}\n".format(error), "red", attrs=["bold"]))
        except ValueError:
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("%s [ERROR] Por favor, ingresar los datos solicitados \n" % datetime.now(), "red", attrs=["bold"]))
        
        return mensaje, clave

    def option(self):
        try:            
            while True:
                opcion = input("[**] Elige una opción > ")
                if opcion:
                    break
                print(colored("%s [INFO] Seleccionar una opción del menú \n" % datetime.now(), "red", attrs=["bold"]))
        
        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored(error, "red", attrs=["bold"]))

        return opcion
    
    def menu(self):
        clear()
        banner = header.figlet_format("Cesar")
        print(colored(banner.rstrip("\n"), "red", attrs=["bold"]))        
        try:
            while True:
                print(colored("[01] Encriptar", "green", attrs=["bold"]))
                print(colored("[02] Desencriptar", "green", attrs=["bold"]))
                print(colored("[03] Hackear", "green", attrs=["bold"]))
                print(colored("[04] Salir", 'green', attrs=["bold"]))
                opcion = str()
                cifrado = Cesar()
                opcion = cifrado.option()
                cifrar = bool()
                if opcion == "1" or opcion == "01":
                    print(colored("%s [INFO] Encriptando... " % datetime.now(), "green", attrs=["bold"]))
                    cifrar = True
                    mensaje, clave = cifrado.datos()
                    resultado, mensaje = cifrado.cesar(mensaje, cifrar, clave)
                    print(colored("%s [INFO] %s " % (datetime.now(), mensaje), "green", attrs=["bold"]))
                    print(colored("%s [INFO] %s \n" % (datetime.now(), resultado), "green", attrs=["bold"]))
                elif opcion == "2" or opcion == "02":
                    print(colored("%s [INFO] Desencriptando... " % datetime.now(), "green", attrs=["bold"]))
                    cifrar = False
                    mensaje, clave = cifrado.datos()
                    resultado, mensaje = cifrado.cesar(mensaje, cifrar, clave)
                    print(colored("%s [INFO] %s " % (datetime.now(), mensaje), "green", attrs=["bold"]))
                    print(colored("%s [INFO] %s \n" % (datetime.now(), resultado), "green", attrs=["bold"]))
                elif opcion == "3" or opcion == "02":
                    print(colored("%s [INFO] Hackeando mensaje... " % datetime.now(), "green", attrs=["bold"]))
                    resultado, mensaje = cifrado.hackear()
                    if resultado == None:
                        print(colored("%s [INFO] Posiblemente el mensaje descifrado no es parte del diccionario español \n" % datetime.now(), "green", attrs=["bold"]))                    
                    else:
                        print(colored("%s [INFO] %s " % (datetime.now(), mensaje), "green", attrs=["bold"]))
                        print(colored("%s [INFO] %s \n" % (datetime.now(), resultado), "green", attrs=["bold"]))
                elif opcion == "4" or opcion == "04":                                        
                    clear()
                    break
                else:                    
                    print(colored("%s [INFO] Introduce una opcion valida del menú \n" % datetime.now(), "red", attrs=["bold"]))
        
        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored(error, "red", attrs=["bold"]))
