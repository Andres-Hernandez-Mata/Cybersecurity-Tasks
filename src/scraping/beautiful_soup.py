"""
Uso: Web scraping
Creador: Andrés Hernández Mata
Version: 1.5.0
Python: 3.9.1
Fecha: 10 Mayo 2020
"""

import os
import pyfiglet as header
import logging
from datetime import datetime
from termcolor import colored
from scraping.scraping import Scraping

clear = lambda: os.system("cls" if os.name=="nt" else "clear")
logging.basicConfig(level=logging.INFO, filename="cybersecurity_tasks.log", format="%(asctime)s %(levelname)s:%(message)s")

class Beautiful:

	def option(self):
		try:
			opcion = 0
			while True:
				opcion = input("[**] Elige una opción > ")
				if not opcion:
					print(colored("\n%s [INFO] Seleccionar una opción del menú" % datetime.now(), "red", attrs=["bold"]))
				else:
					break
		
		except Exception as error:
			logging.error(error, exc_info=True)
			print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
			print(colored("%s [ERROR] Introduce un numero entero" % datetime.now(), "red", attrs=["bold"]))
			print(colored("{}\n".format(error), "red", attrs=["bold"]))
	
		return opcion

	def menu(self):
		clear()
		banner = header.figlet_format("Web Scraping")
		print(colored(banner.rstrip("\n"), "red", attrs=["bold"]))
		opcion = 0
		try:
			while True:
				print(colored("[01] Recolección de información", "green", attrs=["bold"]))
				print(colored("[02] Salir", "green", attrs=["bold"]))
				beautiful = Beautiful()
				scraping = Scraping()
				opcion = beautiful.option()
				if opcion == "1" or opcion == "01":					
					scraping.url()
				elif opcion == "2" or opcion == "02":
					clear()
					break
				else:
					print(colored("\n%s [INFO] Introduce una opción valida del menú" % datetime.now(), "red", attrs=["bold"]))
		except Exception as error:
			logging.error(error, exc_info=True)
			print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
			print(colored(error, "red", attrs=["bold"]))
