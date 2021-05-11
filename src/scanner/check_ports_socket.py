"""
Uso: Socket
Creado: Andrés Hernández Mata
Version: 1.1.0
Python: 3.9.1
Fecha: 16 Abril 2020
"""

import socket
import sys
import faker

def checkPortsSocket(ip,portlist):
    #print("IP",ip,type(ip)) #str    
    try:
        for port in portlist:
            sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)#tecnología, protocolo
            sock.settimeout(5)
            result = sock.connect_ex((ip,port)) #
            if result == 0:
                print ("Puerto {}: \t Abierto".format(port))
            else:
                print ("Puerto {}: \t Cerrado".format(port))
            sock.close()
    except socket.error as error:
        print (str(error))
        print ("Error de conexion")
        sys.exit()


