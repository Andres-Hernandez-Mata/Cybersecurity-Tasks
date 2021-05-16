"""
Uso: Cifrado César
Creado: Andrés Hernández Mata
Version: 2.0.0
Python: 3.9.1
Fecha: 10 Mayo 2020
"""

import os
from datetime import datetime
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
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored(error, "red", attrs=["bold"]))        
        
        return resultado, mensaje

    def hackear(self):        
        try:
            while True:            
                mensaje = input("Mensaje > ")                
                if mensaje:
                    break
                print(colored("%s [INFO] El mensaje es un dato obligatorio" % datetime.now(), "red", attrs=["bold"]))        
        
            cifrado = Cesar()
            for clave in range(1, len(mensaje)):    
                resultado, mensaje = cifrado.cesar(mensaje, False, clave)
                print(colored("%s [INFO] Clave #%s %s" % (datetime.now(), clave, resultado), "yellow", attrs=["bold"]))

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
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored(error, "red", attrs=["bold"]))        

        return None, None
    
    def datos(self):
        try:
            while True:            
                mensaje = input("Mensaje > ")
                clave = int(input("Clave > "))
                if mensaje or clave:
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
    
    def menu(self):
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
                cifrado = Cesar()
                opcion = cifrado.option()
                cifrar = bool()

                if opcion == 1:
                    print(colored("\n%s [INFO] Encriptando... " % datetime.now(), "red", attrs=["bold"]))
                    cifrar = True
                    mensaje, clave = cifrado.datos()
                    resultado, mensaje = cifrado.cesar(mensaje, cifrar, clave)
                    print(colored("%s [INFO] %s " % (datetime.now(), mensaje), "red", attrs=["bold"]))
                    print(colored("%s [INFO] %s \n" % (datetime.now(), resultado), "red", attrs=["bold"]))
                elif opcion == 2:
                    print(colored("\n%s [INFO] Desencriptando... " % datetime.now(), "red", attrs=["bold"]))
                    cifrar = False
                    mensaje, clave = cifrado.datos()
                    resultado, mensaje = cifrado.cesar(mensaje, cifrar, clave)
                    print(colored("%s [INFO] %s " % (datetime.now(), mensaje), "red", attrs=["bold"]))
                    print(colored("%s [INFO] %s \n" % (datetime.now(), resultado), "red", attrs=["bold"]))
                elif opcion == 3:
                    print(colored("\n%s [INFO] Hackeando mensaje... " % datetime.now(), "red", attrs=["bold"]))
                    resultado, mensaje = cifrado.hackear()                    
                    if resultado == None:
                        print(colored("%s [INFO] Posiblemente el mensaje descifrado no es parte del diccionario español \n" % datetime.now(), "red", attrs=["bold"]))                    
                    else:
                        print(colored("%s [INFO] %s " % (datetime.now(), mensaje), "red", attrs=["bold"]))
                        print(colored("%s [INFO] %s \n" % (datetime.now(), resultado), "red", attrs=["bold"]))
                elif opcion == 4:                                        
                    clear()
                    break
                else:                    
                    print(colored("%s [INFO] Introduce una opcion valida del menu" % datetime.now(), "red", attrs=["bold"]))
        
        except Exception as error:
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored(error, 'red', attrs=['bold']))