# Cybersecurity Tasks
Proyecto Integrador de Programacion para Ciberseguridad.

## Web Scraping
Web scraping es el proceso de recopilar información desde Internet. Es como copiar el contenido de una página Web y pegarlo en un documento de Word, pero de forma automatizada con un programa.

## Escaneo de Puertos
Un socket funciona estableciendo un enlace de comunicación de red bidireccional entre el extremo del servidor y el programa receptor del cliente.
Los sockets se crean y se utilizan con un sistema de peticiones o de llamadas de función a veces llamados interfaz de programación de aplicaciones de sockets (API, application programming interface).

En conclusión un socket es una interfaz de entrada-salida de datos que permite la intercomunicación entre proceso.

Hay dos tipos de sockets que son especialmente importantes: Streams y Datagrams.

- Los sockets stream son los más utilizados, hacen uso del protocolo TCP, el cual nos provee un flujo de datos bidireccional, secuenciado, sin duplicación de paquetes y libre de errores.
- Los sockets Datagram hacen uso del protocolo UDP, el cual nos provee un flujo de datos bidireccional, pero los paquetes pueden llegar fuera de secuencia, pueden no llegar o contener errores. Se llaman también sockets sin conexión, porque no hay que mantener una conexión activa, como en el caso de sockets stream. Son utilizados por transferencia de información paquete por paquete.

Nmap es un potente escáner de puertos que permite identificar puertos abiertos, cerrados o filtrados, así como programar rutinas para encontrar posibles vulnerabilidades en un host determinado.

## Cifrado de Mensajes
El cifrado César es un algoritmo criptográfico por sustitución que se usó en la antigüedad para enviar mensajes secretos. Consiste en reemplazar cada letra del mensaje original por la letra que está tres posiciones después en el alfabeto. Por ejemplo, la letra a se sustituye por d, la letra b por e, y así sucesivamente. Aunque originalmente este cifrado desplaza tres posiciones (es decir, la llave es 3), puede definirse cualquier tamaño de llave.

## Envío de Correos
Envío de correos con datos adjuntos.

En ocasiones, para algunas tareas en Ciberseguridad y en TI en general, requerimos contar con herramientas para el manejo automatizado de del correo electrónico.

El protocolo SMTP, Simple Mail Transfer Protocol, es usado para el envío de correo electrónico ya que indica el formato que deben tener los mensajes de correo electrónico, como deben encriptarse, y como debe ser retransmitido entre los servidores de correo y todos los demás detalles que maneja su equipo después de hacer clic en Enviar.

## Obtención de Metadatos
Los metadatos Exif (Exchangeable image file format) son datos que se adjuntan a las fotografías tomadas por cámaras digitales (incluyendo las de los teléfonos). Entre los datos que se guardan en Exif están la información de fecha y hora en que se tomó la fotografía, el modelo de cámara, la velocidad del obturador, la distancia focal, etc. Cuando la cámara está provista con un GPS también puede registrar los datos de geolocalización, como la latitud y la longitud. Este tipo de información puede resultar de utilidad durante una investigación digital o análisis forense informático.

## API de Shodan
Shodan es un motor de búsqueda que se encarga de rastrear servidores y diversos tipos de dispositivos en Internet, extrayendo información útil sobre los servicios que se encuentran en ejecución en dichos objetivos.

Shodan no busca contenido web, sino que busca entra las cabeceras de las peticiones HTTP información sobre el servidor.

## Uso de Windows PowerShell
Powershell es una potencia para la explotación posterior de una máquina con Windows y puede hacer algunas cosas interesantes como descargar los correos electrónicos de los usuarios de ADFS y ayudar con la escalada de privilegios del usuario.

- Microsoft PowerShell es un lenguaje de desarrollo, automatización universal y scripting. Se considera un puente para cerrar la brecha entre estas tareas.
- PowerShell es de código libre y multiplataforma. 
- Contiene, dentro de sus comandos, los comandos de CMD.

## Scapy Dot11
Scapy es una librería realizada en Python, con su propio interprete de línea de comandos (CLI), que permite crear, modificar, enviar y capturar paquetes de red. Se puede utilizar de manera interactiva mediante dicha interfaz o como librería importándola en programas de Python. Se puede ejecutar en sistemas Linux, Mac OS x y Windows.

Aplicado al ámbito de la seguridad informática, esta herramienta nos permite realizar escaneos y/o ataques de red.

La principal ventaja de Scapy es que, a diferencia de otras herramientas, nos proporciona la capacidad  de modificar los paquetes de red a bajo nivel, permitiéndonos utilizar los protocolos de red existentes y parametrizarlos en base a nuestras necesidades.

Y en el caso de que decidamos utilizar sus librerías en Python, podremos desarrollar nuestras propias herramientas, y de esta forma, podríamos realizar otros desarrollos de más alto nivel e integrarlos todos en función de nuestras necesidades.

## Hash SHA512
Una función hash es una función que convierte una cadena de texto de cualquier longitud en una cadena de longitud fija o valor hash. Una característica de un valor hash es que no puede ser revertido para obtener la cadena original. Otra característica es que dos cadenas distintas no deben resultar en el mismo valor hash (colisión). Un hash empleado en criptografía debe tener una tasa de colisiones muy baja para ser confiable.

El módulo hashlib (incluido en la distribución estándar de Python) proporciona implementaciones de diferentes algoritmos criptográficos de hash,

## Sistema Operativo
- Windows 10
- Linux

## Versión
- Python 3.9.1

## Instalación
```python	

> pip install -r requirements.txt

```

## Ejecución
Ejecutar el script que se encuentra en la carpeta src del repositorio.

```python	

> python main.py

```
