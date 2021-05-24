"""
Uso: Nmap
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.8.5
Fecha: 22 Mayo 2021
"""

import nmap
import logging
from datetime import datetime
from termcolor import colored

logging.basicConfig(level=logging.INFO, filename="cybersecurity_tasks.log", format="%(asctime)s %(levelname)s:%(message)s")

class ScannerNmap:

    def range_ip(self):
        try:
            while True:
                print(colored("{} [INFO] Ejemplo IP's > 192.168.100.0-24".format(datetime.now()), "green", attrs=["bold"]))
                ips = input("\nIP's > ")
                if not ips:                    
                    print(colored("{} [INFO] El rango de las IP's es un dato obligatorio".format(datetime.now()), "green", attrs=["bold"]))
                else:
                    break
        
        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}\n".format(error), "red", attrs=["bold"]))
        
        return ips
    
    def scanner_nmap(self):
        try:
            scanner_nmap = ScannerNmap()
            ip = scanner_nmap.range_ip()
            scanner = nmap.PortScanner()
            print(colored("{} [INFO] Escaneando...".format(datetime.now()), "green", attrs=["bold"]))
            scanner.scan(ip,arguments="--open")
            for host in scanner.all_hosts():
                print("--------------------------------------------------------------------------------------")
                print(colored("{} [INFO] Host: {}".format(datetime.now(), host), "green", attrs=["bold"]))
                print(colored("{} [INFO] State: {}".format(datetime.now(), scanner[host].state()), "green", attrs=["bold"]))
                for proto in scanner[host].all_protocols():
                    print("--------------------------------------------------------------------------------------")
                    print(colored("{} [INFO] Protocol: {}".format(datetime.now(), proto), "cyan", attrs=["bold"]))
                    lport = scanner[host][proto].keys()
                    for port in lport:                    
                        print(colored("{} [INFO] Port: {}\tState: {}\tName: {}".format(datetime.now(), port, scanner[host][proto][port]["state"], scanner[host][proto][port]["name"]), "cyan", attrs=["bold"]))        
            print()
            file = open("nmap.csv","w")
            file.write(scanner.csv())

        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}\n".format(error), "red", attrs=["bold"]))