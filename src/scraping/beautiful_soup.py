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
from opcion.menu_opcion import Opcion

clear = lambda: os.system("cls" if os.name=="nt" else "clear")
logging.basicConfig(level=logging.INFO, filename="cybersecurity_tasks.log", format="%(asctime)s %(levelname)s:%(message)s")
opcion = Opcion()
global opcion_menu

class Beautiful:

	def menu(self):
		clear()
		banner = header.figlet_format("Web Scraping")
		print(colored(banner.rstrip("\n"), "red", attrs=["bold"]))
		try:
			while True:
				print(colored("[01] Recolección de información", "green", attrs=["bold"]))
				print(colored("[02] Salir", "green", attrs=["bold"]))
				scraping = Scraping()
				opcion_menu = opcion.opcion()
				if opcion_menu == "1" or opcion_menu == "01":					
					scraping.url()
				elif opcion_menu == "2" or opcion_menu == "02":
					clear()
					break
				else:
					print(colored("%s [INFO] Introduce una opción valida del menú \n" % datetime.now(), "red", attrs=["bold"]))
		except Exception as error:
			logging.error(error, exc_info=True)
			print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
			print(colored("{}\n".format(error), "red", attrs=["bold"]))
