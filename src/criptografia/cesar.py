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
from criptografia.spanish import Spanish

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
                        print(datetime.now(), "\033[0;32m [INFO] Encriptando mensaje... \033[0;0m")
                        indice_nuevo = indice_simbolo + int(clave)
                    # Desencriptar
                    elif not modo:
                        print(datetime.now(), "\033[0;32m [INFO] Desencriptando mensaje... \033[0;0m")
                        indice_nuevo = indice_simbolo - int(clave)

                    if indice_nuevo >= len(simbolos):
                        indice_nuevo = indice_nuevo - len(simbolos)
                    elif indice_nuevo < 0:
                        indice_nuevo = indice_nuevo + len(simbolos)
                    resultado = resultado + simbolos[indice_nuevo]
                else:
                    resultado = resultado + simbolo    
        
        except Exception as error:
            print(colored("[ERROR] Ha ocurrido un error", "red", attrs=["bold"]))
            print(colored(error, "red", attrs=["bold"]))        
        
        return resultado, mensaje

    def hackear():        
        try:

            while True:            
                mensaje = input("Mensaje > ")                
                if not mensaje:
                    break
                print(colored("[INFO] El mensaje es un dato obligatorio", "red", attrs=["bold"]))        
        
            for clave in range(1, len(mensaje)):        
                decrypted_text = cesar(False)
                print(datetime.now(), "\033[0;32m [INFO] Clave #%s \033[0;0m %s" % (clave, decryptedText))

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
            print(colored("[ERROR] Ha ocurrido un error", "red", attrs=["bold"]))
            print(colored(error, "red", attrs=["bold"]))        

        return None
    
    def datos():
        try:

            while True:            
                mensaje = input("Mensaje > ")
                clave = int(input("Clave > "))
                if not mensaje or not clave:
                    break
                print(colored("[INFO] El mensaje y clave son datos obligatorios", "red", attrs=["bold"]))
        
        except ValueError:
            print(colored("[ERROR] Ha ocurrido un error", "red", attrs=["bold"]))
            print(colored("[ERROR] Por favor, ingresar los datos solicitados", "red", attrs=["bold"]))
        
        return mensaje, clave

    def selecciona():
        try:

            opcion = 0
            while True:                
                opcion = int(input("[**] Elige una opción > "))
                if not opcion:
                    break
                print(colored("[INFO] Seleccionar una opcion del menu", "red", attrs=["bold"]))
        except ValueError:
            print(colored("[ERROR] Ha ocurrido un error", "red", attrs=["bold"]))
            print(colored("[ERROR] Por favor, ingresar los datos solicitados", "red", attrs=["bold"]))

        return opcion
    
    def menu():
        opcion = 0
        try:
            while True:
                print(colored("[01] Encriptar", "green", attrs=["bold"]))
                print(colored("[02] Desencriptar", "green", attrs=["bold"]))
                print(colored("[03] Hackear", "green", attrs=["bold"]))
                print(colored("[04] Salir", 'green', attrs=["bold"]))
                opcion = selecciona()
                cifrar = bool()

                if opcion == 1:
                    print(datetime.now(), "\033[0;32m [INFO] Iniciando... \033[0;0m")
                    cifrar = True
                    mensaje, clave = datos()
                    resultado, mensaje = cesar(mensaje, cifrar, clave)
                    print(datetime.now(), "\033[0;33m [INFO] %s \033[0;0m" % mensaje)
                    print(datetime.now(), "\033[0;36m [INFO] %s \033[0;0m" % resultado)
                elif opcion == 2:
                    print(datetime.now(), "\033[0;32m [INFO] Iniciando... \033[0;0m")
                    cifrar = False
                    mensaje, clave = datos()
                    resultado, mensaje = cesar(mensaje, cifrar, clave)
                    print(datetime.now(), "\033[0;33m [INFO] %s \033[0;0m" % mensaje)
                    print(datetime.now(), "\033[0;36m [INFO] %s \033[0;0m" % resultado)
                elif opcion == 3:
                    print(datetime.now(), "\033[0;32m [INFO] Hackeando mensaje... \033[0;0m")
                    resultado, mensaje = hackear()
                    if resultado == None:
                        print(datetime.now(), "\033[0;91m [INFO] El mensaje descifrado no es parte del idioma en español \033[0;0m")
                    print(datetime.now(), "\033[0;33m [INFO] %s \033[0;0m" % mensaje)        
                    print(datetime.now(), "\033[0;36m [INFO] %s \033[0;0m" % resultado)    
                elif opcion == 4:                                        
                    print(colored("[INFO] Bye...", 'red', attrs=['bold']))
                    break
                else:                    
                    print(colored("[INFO] Introduce una opcion valida del menu", 'red', attrs=['bold']))
        except Exception as error:
            print(colored(error, 'red', attrs=['bold']))
