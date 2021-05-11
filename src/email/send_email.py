"""
Uso: Envío de correos con datos adjuntos
Creado: Andrés Hernández Mata
Version: 1.5.0
Python: 3.9.1
Fecha: 03 Mayo 2020
"""

import email, smtplib, ssl
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from os.path import basename
from datetime import datetime
import os
import pathlib

def main():
    os.system("cls")
    print(datetime.now(), "\033[0;32m [INFO] Envío de correos con datos adjuntos \033[0;0m")
    print(datetime.now(), "\033[0;32m [INFO] Iniciar sesión ... \033[0;0m \n")

    while(True):        
        sender_email = input("From > ")    
        password = getpass.getpass("Password > ")
        if not sender_email or not password:
            os.system("cls")
            print(datetime.now(), "\033[0;31m [INFO] Iniciar sesión \033[0;0m")
            print(datetime.now(), "\033[0;31m [INFO] From y password son datos obligatorios \033[0;0m \n")
        else:
            break        
    
    while(True):        
        receiver_email = input("To > ")
        if not receiver_email:
            os.system("cls")
            print(datetime.now(), "\033[0;31m [INFO] La dirección de destino es un dato obligatorio \033[0;0m \n")
        else:
            break
        
    subject = input("Subject > ")    
    body = input("Body > ")

    try:
        while(True):
            image = input("Imagen > ")
            pathImage = pathlib.Path(image)
            if not image:
                os.system("cls")
                print(datetime.now(), "\033[0;31m [INFO] La imagen es un dato obligatorio \033[0;0m \n")
            elif not pathImage.exists():
                os.system("cls")
                print(datetime.now(), "\033[0;31m [INFO] La imagen ingresa no existe en el sistema \033[0;0m \n")
            else:
                break
    except Exception as error:
        print(datetime.now(), "\033[0;91m [ERROR] Ha ocurrido un error")
        print(error)

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
    msgHtml = MIMEText(html, 'html')

    img = open(image, 'rb').read()
    msgImage = MIMEImage(img)
    msgImage.add_header('Content-ID', '<image>')
    msgImage.add_header('Content-Disposition', 'inline', filename=os.path.basename(image))
          
    message.attach(msgHtml)
    message.attach(msgImage)

    context = ssl.create_default_context()
    try:
        print()
        print(datetime.now(), "\033[0;32m [INFO] Enviando correo electronico... \033[0;0m")
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)        
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print(datetime.now(), "\033[0;32m [INFO] Correo enviado! \033[0;0m")
    except Exception as error:
        print(datetime.now(), "\033[0;91m [ERROR] Ha ocurrido un error")
        print(error)
    finally:        
        server.quit()

if __name__ == '__main__':
    main()