"""
Uso: Cifrado César
Creado: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 10 Mayo 2020
"""

import argparse
import os
from datetime import datetime
import detect_spanish

def main():
    os.system("cls")
    print(datetime.now(), "\033[0;32m [INFO] Iniciando... \033[0;0m")
    description = """Example -modo e -mensaje 'Hola Mundo' -clave 3 \nExample -modo d -mensaje 'Krod Pxqgr' -clave 3 \nExample -modo h -mensaje 'Hola Mundo'"""
    parser = argparse.ArgumentParser(description='Cifrado cesar', epilog=description, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-modo", metavar='--modo', dest="modo", help="Modo para e (encriptar), d (desencriptar) o h (hackear)", required=True)
    parser.add_argument("-mensaje", metavar='--mensaje', dest="mensaje", help="Mensaje para cifrar, desencriptar o para hackear", required=True)
    parser.add_argument("-clave", metavar='--clave', dest="clave", help="Clave para cifrar o descifrar el mensaje, default clave 3", default="3")
    params = parser.parse_args()
    
    if params.modo == 'e':
        print(datetime.now(), "\033[0;32m [INFO] Encriptando mensaje... \033[0;0m")
        resultado = cesar(params.mensaje,True,params.clave)
        print(datetime.now(), "\033[0;33m [INFO] %s \033[0;0m" % params.mensaje)
        print(datetime.now(), "\033[0;36m [INFO] %s \033[0;0m" % resultado)
    elif params.modo == 'd':
        print(datetime.now(), "\033[0;32m [INFO] Desencriptando mensaje... \033[0;0m")
        resultado = cesar(params.mensaje,False,params.clave)
        print(datetime.now(), "\033[0;33m [INFO] %s \033[0;0m" % params.mensaje)
        print(datetime.now(), "\033[0;36m [INFO] %s \033[0;0m" % resultado)
    elif params.modo == 'h':
        print(datetime.now(), "\033[0;32m [INFO] Hackeando mensaje... \033[0;0m")
        resultado = hackear(params.mensaje)
        print(datetime.now(), "\033[0;33m [INFO] %s \033[0;0m" % params.mensaje)
        if resultado == None:
            print(datetime.now(), "\033[0;91m [INFO] El mensaje descifrado no es parte del idioma en español \033[0;0m")
            quit()
        print(datetime.now(), "\033[0;36m [INFO] %s \033[0;0m" % resultado)    
    else:
        print(datetime.now(), "\033[0;91m [INFO] Seleccione el modo correcto... \033[0;0m")        
        quit()

    print(datetime.now(), "\033[0;32m [INFO] Success \033[0;0m")

def hackear(mensaje):
    for clave in range(1, len(mensaje)):        
        decryptedText = cesar(mensaje,False,clave)
        print(datetime.now(), "\033[0;32m [INFO] Clave #%s \033[0;0m %s" % (clave, decryptedText))

        if detect_spanish.isSpanish(decryptedText):
            print()
            print('Posible mensaje descifrado:')
            print('Clave %s: %s' % (clave, decryptedText[:100]))
            print()
            print('¿Si?')
            response = input('> ')
            print()

            if response.strip().upper().startswith('SI'):
                return decryptedText

    return None

def cesar(mensaje,modo,clave):
    simbolos = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    resultado = ''
    
    try:
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
        print(datetime.now(), "\033[0;91m [ERROR] Ha ocurrido un error")
        print(error)
        quit()
    
    return resultado

if __name__ == "__main__":    
    main()

