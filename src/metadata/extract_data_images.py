"""
Uso: Metadata de imagenes
Creador: Andrés Hernández Mata
Version: 3.0.0
Python: 3.9.1
Fecha: 10 Mayo 2021
"""

import os
import pathlib
import logging
from PIL.ExifTags import TAGS
from PIL import Image
from termcolor import colored
from datetime import datetime

logging.basicConfig(level=logging.INFO, filename="cybersecurity_tasks.log", format="%(asctime)s %(levelname)s:%(message)s")
class Imagenes:

    def decode_gps_info(self, exif):       
        try:
            if "GPSInfo" in exif:
                Nsec = exif["GPSInfo"][2][2] 
                Nmin = exif["GPSInfo"][2][1]
                Ndeg = exif["GPSInfo"][2][0]
                Wsec = exif["GPSInfo"][4][2]
                Wmin = exif["GPSInfo"][4][1]
                Wdeg = exif["GPSInfo"][4][0]
                if exif["GPSInfo"][1] == "N":
                    Nmult = 1
                else:
                    Nmult = -1
                if exif["GPSInfo"][3] == "E":
                    Wmult = 1
                else:
                    Wmult = -1
                Lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
                Lng = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)
                exif["GPSInfo"] = {"Lat" : Lat, "Lng" : Lng}
        
        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}".format(error), "red", attrs=["bold"]))            
    
    def get_exif_metadata(self, image_path):
        try:
            imagenes = Imagenes()
            ret = {}
            image = Image.open(image_path)
            if hasattr(image, "_getexif"):
                exif_info = image._getexif()
                if exif_info is not None:
                    for tag, value in exif_info.items():
                        decoded = TAGS.get(tag, tag)
                        ret[decoded] = value
            imagenes.decode_gps_info(ret)            
            return ret
        
        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}".format(error), "red", attrs=["bold"]))

    def get_metadata_imagenes(self):                
        try:
            src = os.getcwd()
            imagenes = Imagenes()
            os.chdir("metadata")
            file = open("metadata_imagenes.txt", "w")
            while True:
                ruta = input("\nRuta de imágenes > ")
                pathRuta = pathlib.Path(ruta)
                if not ruta:
                    print(colored("%s [INFO] La ruta de imágenes es un dato obligatorio " % datetime.now(), "red", attrs=["bold"]))
                elif not pathRuta.exists():                    
                    print(colored("%s [INFO] La ruta de imágenes ingresada no existe en el sistema " % datetime.now(), "red", attrs=["bold"]))
                else:
                    break
            print()
            os.chdir(ruta)
            for root, dirs, files in os.walk(".", topdown=False):               
                for name in files:
                    print(colored("{} [INFO] Metadata de {}".format(datetime.now(), name), "green", attrs=["bold"]))
                    file.write(os.path.join(root, name))
                    file.write(os.linesep)
                    file.write("[+] Metadata for file: %s \n" % (name))
                    exif = imagenes.get_exif_metadata(name)                    
                    for metadata in exif:
                        file.write("Metadata: %s - Value: %s \n" % (metadata, exif[metadata]))
                file.close()
            os.chdir(src)            
            print(colored("%s [INFO] Puedes consultar el resultado obtenido en metadata_imagenes.txt \n" % datetime.now(), "green", attrs=["bold"]))
        
        except Exception as error:
            os.chdir(src)
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}\n".format(error), "red", attrs=["bold"]))
            



