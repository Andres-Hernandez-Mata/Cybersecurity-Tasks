"""
Uso: Metadata de PDF's
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 26 Abril 2021
"""

import os
from PyPDF2 import PdfFileReader
from termcolor import colored
from datetime import datetime

class PDF:

    def get_metadata_pdf():
        try:
            ruta = input("Ruta de pdf's: ")
            os.chdir(ruta)
            for root, dirs, files in os.walk(".", topdown=False):
                for name in files:
                    ext = name.lower().rsplit(".", 1)[-1]
                    print(name.lower().rsplit(".", 1))                    
                    if ext in ["pdf"]:
                        print("[+] Metadata for file: %s " % (ruta+os.path.sep+name))
                        pdfFile = PdfFileReader(open(ruta+os.path.sep+name, "rb"))
                        docInfo = pdfFile.getDocumentInfo()
                        print("Tipo: ", type(docInfo))
                        for metaItem in docInfo:
                            print("[+] " + metaItem + ":" + docInfo[metaItem])
                        print("\n")
        
        except Exception as error:
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}\n".format(error), "red", attrs=["bold"]))
