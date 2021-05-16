"""
Uso: Envío de correos con datos adjuntos
Creador: Andrés Hernández Mata
Version: 2.2.0
Python: 3.9.1
Fecha: 03 Mayo 2021
"""

import smtplib, ssl
import getpass
import os
import pathlib
import pyfiglet as header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from os.path import basename
from datetime import datetime
from termcolor import colored

clear = lambda: os.system("cls" if os.name=="nt" else "clear")

class Correo:  

    def send(self):        
        print(colored("\n%s [INFO] Envío de correos con datos adjuntos" % datetime.now(), "green", attrs=["bold"]))
        print(colored("%s [INFO] Iniciar sesión ...\n" % datetime.now(), "green", attrs=["bold"]))
        while True:        
            sender_email = input("From > ")    
            password = getpass.getpass("Password > ")
            if not sender_email or not password:                
                print(colored("%s [INFO] From y password son datos obligatorios \n" % datetime.now(), "red", attrs=["bold"]))
            else:
                break        
        
        while True:        
            receiver_email = input("To > ")
            if not receiver_email:                
                print(colored("%s [INFO] La dirección de destino es un dato obligatorio \n" % datetime.now(), "red", attrs=["bold"]))
            else:
                break
            
        subject = input("Subject > ")    
        body = input("Body > ")

        try:
            while True:
                image = input("Imagen > ")
                pathImage = pathlib.Path(image)
                if not image:                    
                    print(colored("%s [INFO] La imagen es un dato obligatorio \n" % datetime.now(), "red", attrs=["bold"]))
                elif not pathImage.exists():                    
                    print(colored("%s [INFO] La imagen ingresa no existe en el sistema \n" % datetime.now(), "red", attrs=["bold"]))
                else:
                    break
        
        except Exception as error:
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored(error, "red", attrs=["bold"]))

        nombre = input("Nombre > ")

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        
        html = f"""\
        <html>
        <head></head>
        <body>
            <p>{body}</p>
            <p>{nombre}</p><br>
            <img src="cid:image"><br>        
        </body>
        </html>
        """ 
        msgHtml = MIMEText(html, "html")

        img = open(image, "rb").read()
        msgImage = MIMEImage(img)
        msgImage.add_header("Content-ID", "<image>")
        msgImage.add_header("Content-Disposition", "inline", filename=os.path.basename(image))
            
        message.attach(msgHtml)
        message.attach(msgImage)

        context = ssl.create_default_context()
        try:
            print(colored("\n%s [INFO] Enviando correo electronico..." % datetime.now(), "green", attrs=["bold"]))
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)        
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print(colored("%s [INFO] El correo se envio correctamente" % datetime.now(), "green", attrs=["bold"]))
        
        except Exception as error:
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}\n".format(error), "red", attrs=["bold"]))            
    
    def option(self):
        try:
            opcion = 0
            while True:
                opcion = input("[**] Elige una opción > ")
                if not opcion:
                    print(colored("\n%s [INFO] Seleccionar una opcion del menu" % datetime.now(), "red", attrs=["bold"]))
                else:
                    break    
        
        except Exception as error:
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored("%s [ERROR] Introduce un numero entero" % datetime.now(), "red", attrs=["bold"]))
            print(colored("{}\n".format(error), "red", attrs=["bold"]))
        
        return opcion
    
    def option():
        try:
            opcion = 0
            while True:
                opcion = input("[**] Elige una opción > ")
                if opcion:                
                    break
                print(colored("\n%s [INFO] Seleccionar una opcion del menú" % datetime.now(), "red", attrs=["bold"]))
        
        except Exception as error:
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored(error, "red", attrs=["bold"]))
        
        return opcion
    
    def menu(self):
        clear()
        banner = header.figlet_format("Email")
        print(colored(banner.rstrip("\n"), "red", attrs=["bold"]))
        opcion = 0
        try:
            while True:
                print(colored("[01] Enviar correo electrónico", "green", attrs=["bold"]))
                print(colored("[02] Salir", "green", attrs=["bold"]))
                correo = Correo()
                opcion = correo.option()
                if opcion == "1" or opcion == "01":
                    correo.send()
                elif opcion == "2" or opcion == "02":
                    clear()
                    break
                else:                    
                    print(colored("\n%s [INFO] Introduce una opcion valida del menú" % datetime.now(), "red", attrs=["bold"]))
        
        except Exception as error:
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored(error, "red", attrs=["bold"]))

      
