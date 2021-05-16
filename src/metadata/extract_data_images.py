"""
Uso: Metadata de imagenes
Creador: Andrés Hernández Mata
Version: 2.0.0
Python: 3.9.1
Fecha: 10 Mayo 2021
"""

import os
import sys, traceback
from PIL.ExifTags import TAGS
from PIL import Image
from termcolor import colored
from datetime import datetime

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
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}\n".format(error), "red", attrs=["bold"]))
    
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
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}\n".format(error), "red", attrs=["bold"]))

    def get_metadata_imagenes(self):
        try:
            imagenes = Imagenes()
            file = open("extract_data_imagenes.txt", "w")
            while True:
                ruta = input("\nRuta de imágenes: ")
                if not ruta:
                    print(colored("\n%s [INFO] La ruta de imágenes es un dato obligatorio" % datetime.now(), "red", attrs=["bold"]))
                else:
                    break
            os.chdir(ruta)
            for root, dirs, files in os.walk(".", topdown=False):
                for name in files:
                    file.write(os.path.join(root, name))
                    file.write(os.linesep)
                    file.write("[+] Metadata for file: %s \n" % (name))                    
                    try:                        
                        exif = imagenes.get_exif_metadata(name)
                        for metadata in exif:
                            file.write("Metadata: %s - Value: %s \n" %(metadata, exif[metadata]))                    
                    except:                        
                        traceback.print_exc(file=sys.stdout)
            print(colored("%s [INFO] Puedes consultar el resultado obtenido en extract_data_imagenes.txt" % datetime.now(), "green", attrs=["bold"]))
        
        except Exception as error:
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}\n".format(error), "red", attrs=["bold"]))
        finally:
            file.close()



