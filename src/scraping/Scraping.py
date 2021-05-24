"""
Uso: Web scraping
Creador: Andrés Hernández Mata
Version: 2.0.0
Python: 3.9.1
Fecha: 10 Mayo 2020
"""

import os
import requests
import logging
from lxml import html
import pathlib
from bs4 import BeautifulSoup
from datetime import datetime
from termcolor import colored

clear = lambda: os.system("cls" if os.name=="nt" else "clear")
logging.basicConfig(level=logging.INFO, filename="cybersecurity_tasks.log", format="%(asctime)s %(levelname)s:%(message)s")

class Scraping:
    
    def scraping_beautiful_soup(self, url, response):    
        try:
            print(colored("\n%s [INFO] Obteniendo las imágenes de %s" % (datetime.now(), url), "green", attrs=["bold"]))            
            bs = BeautifulSoup(response.text, "lxml")
            parsed_body = html.fromstring(response.text)
            images = parsed_body.xpath("//img/@src")
            print(colored("%s [INFO] %s imágenes encontradas" % (datetime.now(), len(images)), "green", attrs=["bold"]))
            #Create directory for save images
            os.chdir("scraping")
            carpeta_images = pathlib.Path("imagenes")
            if carpeta_images.exists():
                print(colored("%s [INFO] Almacenando las imágenes en la carpeta imagenes" % datetime.now(), "green", attrs=["bold"]))
            else:               
                os.system("mkdir imagenes")
                print(colored("%s [INFO] Creando carpeta para guardar las imágenes" % datetime.now(), "green", attrs=["bold"]))
                print(colored("%s [INFO] Nueva carpeta llamada imagenes" % datetime.now(), "green", attrs=["bold"]))
            for tagImage in bs.find_all("img"):                 
                if tagImage["src"].startswith("http") == False:
                    download = url + tagImage["src"]
                else:
                    download = tagImage["src"]                
                #Download images in img directory
                request = requests.get(download, verify=False)
                file = open("imagenes/%s" % download.split("/")[-1], "wb")
                file.write(request.content)
                file.close()
        
        except Exception as error:
            logging.error(error, exc_info=True)           
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}\n".format(error), "red", attrs=["bold"]))      
            
    def scraping_pdf(self, url, response):        
        print(colored("%s [INFO] Obteniendo los pdf's de %s" % (datetime.now(), url), "green", attrs=["bold"]))
        try:            
            parsed_body = html.fromstring(response.text)
            #Expresion regular para obtener pdf
            pdfs = parsed_body.xpath('//a[@href[contains(., ".pdf")]]/@href')    
            #Create directory for save pdfs
            if len(pdfs) > 0:
                print(colored("%s [INFO] %s pdf's encontrados" % (datetime.now(), len(pdfs)), "green", attrs=["bold"]))
                carpeta_pdfs = pathlib.Path("pdfs")
                if carpeta_pdfs.exists():
                    print(colored("%s [INFO] Almacenando los pdf's en la carpeta pdfs" % datetime.now(), "green", attrs=["bold"]))
                else:
                    os.system("mkdir pdfs")
                    print(colored("%s [INFO] Creando carpeta para guardar los pdf's" % datetime.now(), "green", attrs=["bold"]))
                    print(colored("%s [INFO] Nueva carpeta llamada pdfs" % datetime.now(), "green", attrs=["bold"]))
                            
            for pdf in pdfs:
                if pdf.startswith("http") == False:
                    download = url + pdf
                else:
                    download = pdf                    
                #Descarga pdfs
                request = requests.get(download, verify=False)
                file = open("pdfs/%s" % download.split("/")[-1], "wb")
                file.write(request.content)
                file.close()            
                
        except Exception as error:
            logging.error(error, exc_info=True)          
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}\n".format(error), "red", attrs=["bold"]))                    

    def scraping_links(self, url, response):        
        print(colored("%s [INFO] Obteniendo los links de %s" % (datetime.now(), url), "green", attrs=["bold"]))
        try:            
            parsed_body = html.fromstring(response.text)    
            #Expresion regular para obtener links
            links = parsed_body.xpath('//a/@href')
            print(colored("%s [INFO] %s links encontrados " % (datetime.now(), len(links)), "green", attrs=["bold"]))            
            file = open("links.txt","w")
            for link in links:                
                if link.startswith("http") or link.startswith("https"):
                    file.write("{} \n".format(link))                   
            print(colored("%s [INFO] Puedes consultar la información obtenida en links.txt \n" % datetime.now(), "green", attrs=["bold"]))
            os.chdir("..")  
        
        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}\n".format(error), "red", attrs=["bold"]))
    
    def requests_get(self, url):
        try:
            scraping = Scraping()
            response = requests.get(url, verify=False)
            scraping.scraping_beautiful_soup(url, response)
            scraping.scraping_pdf(url, response)
            scraping.scraping_links(url, response)

        except Exception as error:
            logging.error(error, exc_info=True)     
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}\n".format(error), "red", attrs=["bold"]))

    def url(self):
        try:
            scraping = Scraping()
            while True:
                url = input("\nURL > ")
                if not url:
                    print(colored("%s [INFO] La url es un dato obligatorio" % datetime.now(), "red", attrs=["bold"]))
                else:
                    break
            scraping.requests_get(url)

        except Exception as error:
            logging.error(error, exc_info=True)     
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}\n".format(error), "red", attrs=["bold"]))

