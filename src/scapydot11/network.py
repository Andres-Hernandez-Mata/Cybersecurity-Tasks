"""
Uso: Escáner de punto de acceso con su seguridad Wi-Fi
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.8.5
Fecha: 21 Mayo 2021
"""

from scapy.all import Ether, ARP, srp
import logging
from datetime import datetime
from termcolor import colored


logging.basicConfig(level=logging.INFO, filename="cybersecurity_tasks.log", format="%(asctime)s %(levelname)s:%(message)s")

class Network:  	
	
	def ip(self):
		try:
			while True:
				ip = input("\nIP > ")
				if not ip:
					print(colored("%s [INFO] La IP es un dato obligatorio" % datetime.now(), "red", attrs=["bold"]))
				else:
					break

		except Exception as error:
			logging.error(error, exc_info=True)
			print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
			print(colored("{}\n".format(error), "red", attrs=["bold"]))
		
		return ip

	def mac_address(self):
		try:
			network = Network()
			ip = network.ip()
			request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
			ans, unans = srp(request, timeout=2, retry=1)
			for sent, received in ans:
				print(colored("{} [INFO] IP > {} MAC > {} \n".format(datetime.now(), received.psrc, received.hwsrc), "green", attrs=["bold"]))

		except Exception as error:
			logging.error(error, exc_info=True)
			print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
			print(colored("{}\n".format(error), "red", attrs=["bold"]))
