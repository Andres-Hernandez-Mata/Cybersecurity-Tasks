"""
Uso: Cifrado César
Creado: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 10 Mayo 2020
"""

import os
from datetime import datetime
from colorama import Fore
from colorama import Style
import pyfiglet as header
from termcolor import colored
from cifrado.spanish import Spanish

clear = lambda: os.system("cls" if os.name=="nt" else "clear")
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
                        print("%s [INFO] Encriptando mensaje... " % datetime.now())
                        indice_nuevo = indice_simbolo + int(clave)
                    # Desencriptar
                    elif not modo:
                        print("%s [INFO] Desencriptando mensaje... " % datetime.now())
                        indice_nuevo = indice_simbolo - int(clave)

                    if indice_nuevo >= len(simbolos):
                        indice_nuevo = indice_nuevo - len(simbolos)
                    elif indice_nuevo < 0:
                        indice_nuevo = indice_nuevo + len(simbolos)
                    resultado = resultado + simbolos[indice_nuevo]
                else:
                    resultado = resultado + simbolo    
        
        except Exception as error:
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored(error, "red", attrs=["bold"]))        
        
        return resultado, mensaje

    def hackear():        
        try:
            while True:            
                mensaje = input("Mensaje > ")                
                if not mensaje:
                    break
                print(colored("%s [INFO] El mensaje es un dato obligatorio" % datetime.now(), "red", attrs=["bold"]))        
        
            for clave in range(1, len(mensaje)):        
                decrypted_text = cesar(False)
                print("%s [INFO] Clave #%s \033[0;0m %s" % (datetime.now(), clave, decryptedText))

                detect_spanish = Spanish()
                if detect_spanish.spanish(decrypted_text):
                    print()
                    print("Posible mensaje descifrado: ")
                    print("Clave %s: %s" % (clave, decrypted_text[:100]))
                    print()
                    print("¿Si?")
                    response = input("> ")
                    print()

                    if response.strip().upper().startswith("SI"):
                        return decrypted_text, mensaje

        except Exception as error:
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored(error, "red", attrs=["bold"]))        

        return None
    
    def datos():
        try:
            while True:            
                mensaje = input("Mensaje > ")
                clave = int(input("Clave > "))
                if not mensaje or not clave:
                    break
                print(colored("%s [INFO] El mensaje y clave son datos obligatorios" % datetime.now(), "red", attrs=["bold"]))
        
        except Exception as error:
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored(error, "red", attrs=["bold"]))
        except ValueError:
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("%s [ERROR] Por favor, ingresar los datos solicitados" % datetime.now(), "red", attrs=["bold"]))
        
        return mensaje, clave

    def option(self):
        try:
            opcion = 0
            while True:
                opcion = int(input("[**] Elige una opción > "))
                if opcion:
                    break
                print(colored("%s [INFO] Seleccionar una opcion del menu" % datetime.now(), "red", attrs=["bold"]))
        
        except Exception as error:
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored(error, "red", attrs=["bold"]))
        except ValueError:
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("%s [ERROR] Por favor, ingresar los datos solicitados" % datetime.now(), "red", attrs=["bold"]))

        return opcion
    
    def menu():
        clear()
        banner = header.figlet_format("Cesar")
        print(colored(banner.rstrip("\n"), "red", attrs=["bold"]))
        opcion = 0
        try:
            while True:
                print(colored("[01] Encriptar", "green", attrs=["bold"]))
                print(colored("[02] Desencriptar", "green", attrs=["bold"]))
                print(colored("[03] Hackear", "green", attrs=["bold"]))
                print(colored("[04] Salir", 'green', attrs=["bold"]))
                cesar = Cesar()
                opcion = cesar.option()
                cifrar = bool()

                if opcion == 1:
                    print("%s [INFO] Iniciando... " % datetime.now())
                    cifrar = True
                    mensaje, clave = cesar.datos()
                    resultado, mensaje = cesar(mensaje, cifrar, clave)
                    print("%s [INFO] %s " % (datetime.now(), mensaje))
                    print("%s [INFO] %s " % (datetime.now(), resultado))
                elif opcion == 2:
                    print("%s [INFO] Iniciando... " % datetime.now())
                    cifrar = False
                    mensaje, clave = cesar.datos()
                    resultado, mensaje = cesar(mensaje, cifrar, clave)
                    print("%s [INFO] %s " % (datetime.now(), mensaje))
                    print("%s [INFO] %s " % (datetime.now(), resultado))
                elif opcion == 3:
                    print("%s [INFO] Hackeando mensaje... " % datetime.now())
                    resultado, mensaje = cesar.hackear()
                    if resultado == None:
                        print("%s [INFO] El mensaje descifrado no es parte del idioma en español" % datetime.now())
                    print("%s [INFO] %s " % (datetime.now(), mensaje))
                    print("%s [INFO] %s " % (datetime.now(), resultado))
                elif opcion == 4:                                        
                    print(colored("%s [INFO] Bye..." % datetime.now(), 'red', attrs=['bold']))
                    break
                else:                    
                    print(colored("%s [INFO] Introduce una opcion valida del menu" % datetime.now(), "red", attrs=["bold"]))
        
        except Exception as error:
            print(colored(error, 'red', attrs=['bold']))
