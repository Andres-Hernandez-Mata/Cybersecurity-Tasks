"""
Uso: Escanear puertos
Creado: Andrés Hernández Mata
Version: 1.1.0
Python: 3.9.1
Fecha: 16 Abril 2020
"""

import argparse
import requests
import check_ports_socket
import os

os.system("cls")

if __name__ == "__main__":

    description = """ Ejemplos de uso:
        + Escaneo basico:
             -target 127.0.0.1
        + Indica un puerto especifico:
             -target 127.0.0.1 -port 21
        + Indica una lista de puertos:
             -target 127.0.0.1 -port 21,22"""

    parser = argparse.ArgumentParser(description='Port scanning', epilog=description,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-target", metavar='TARGET', dest="target", help="target to scan",required=True)
    parser.add_argument("-ports", dest="ports", 
                        help="Please, specify the target port(s) separated by comma[80,8080 by default]",
                        default = "80,8080")    
    params = parser.parse_args()
	#python scanner_puertos.py -target 192.168.100.38 -port 22,25,80
	# -target (socket) --> la necesito en str y la recibo en str ==> =D
    # -ports (c/u) --> int
    portlist = params.ports.split(',') # lista de str
    #print (params.ports) #["22","25","80"]
    #print (portlist) # "22,25,80"
    for i in range(len(portlist)):
        #print ("Puerto:" + portlist[i])
        portlist[i] = int(portlist[i]) #lista de int
    #módulo.función(parámetros)
    check_ports_socket.checkPortsSocket(params.target,portlist)
