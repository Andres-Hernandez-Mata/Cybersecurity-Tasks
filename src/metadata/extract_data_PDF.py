"""
Uso: Metadata de PDF's
Creador: Andrés Hernández Mata
Version: 3.7.0
Python: 3.9.1
Fecha: 26 Abril 2021
"""

import os
import pathlib
import logging
from PyPDF2 import PdfFileReader
from termcolor import colored
from datetime import datetime

logging.basicConfig(level=logging.INFO, filename="cybersecurity_tasks.log", format="%(asctime)s %(levelname)s:%(message)s")

class Documentos:

    def get_metadata_pdf(self):
        try:
            src = os.getcwd()
            os.chdir("metadata")         
            file = open("metadata_pdfs.txt", "w")
            while True:
                ruta = input("\nRuta de pdf's > ")
                pathRuta = pathlib.Path(ruta)
                if not ruta:
                    print(colored("%s [INFO] La ruta de pdf's es un dato obligatorio " % datetime.now(), "red", attrs=["bold"]))
                elif not pathRuta.exists():                    
                    print(colored("%s [INFO] La ruta de pdf's ingresada no existe en el sistema " % datetime.now(), "red", attrs=["bold"]))
                else:
                    break
            print()
            os.chdir(ruta)
            for root, dirs, files in os.walk(".", topdown=False):
                for name in files:
                    print(colored("{} [INFO] Metadata de {}".format(datetime.now(), name), "green", attrs=["bold"]))
                    ext = name.lower().rsplit(".", 1)[-1]                    
                    if ext in ["pdf"]:
                        file.write("[+] Metadata for file: %s \n" % (ruta+os.path.sep+name))
                        pdfFile = PdfFileReader(open(ruta+os.path.sep+name, "rb"))
                        docInfo = pdfFile.getDocumentInfo()                       
                        for metaItem in docInfo:
                            file.write("[+] {} : {} \n".format(metaItem, docInfo[metaItem]))
            os.chdir(src)
            print(colored("%s [INFO] Puedes consultar el resultado obtenido en metadata_pdfs.txt \n" % datetime.now(), "green", attrs=["bold"]))
        
        except Exception as error:
            os.chdir(src)
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}\n".format(error), "red", attrs=["bold"]))
