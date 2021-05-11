"""
Uso: Metadata de PDF's
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 26 Abril 2020
"""

from PyPDF2 import PdfFileReader, PdfFileWriter
import os 

def printMeta():
    ruta = input("Ruta de pdf: ")
    os.chdir(ruta)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            ext = name.lower().rsplit('.', 1)[-1] #archivo.nombre.algo.pdf
            print(name.lower().rsplit('.', 1))
            input()
            if ext in ['pdf']:
                print("[+] Metadata for file: %s " %(ruta+os.path.sep+name))
                pdfFile = PdfFileReader(open(ruta+os.path.sep+name, 'rb'))
                docInfo = pdfFile.getDocumentInfo()
                print("Tipo: ", type(docInfo)) 
                for metaItem in docInfo:
                    print('[+] ' + metaItem + ':' + docInfo[metaItem])
                print("\n")
printMeta()
