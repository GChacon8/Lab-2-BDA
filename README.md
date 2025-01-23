CONFIGURACION DE MONGO DB:
1. Descargar el comprimido (.zip) desde la página oficial de mongodb, en nuestro caso la versión “Community Server” en el siguiente enlace: https://www.mongodb.com/try/download/community
2. Descomprimir el archivo comprimido
3. En una terminal, navega al directorio donde se descomprimió la carpeta bin de mongodb.
4. Ejecutar el servidor de MongoDB con el siguiente comando:

$mongod.exe --dbpath “dir”

Esto iniciará el servidor MongoDB utilizando el directorio especificado como el lugar donde almacenará los datos.
Notas importantes:
- Asegurarse de que la dirección del directorio de datos existe antes de ejecutar el comando, sino crearla manualmente
- Se debe mantener esta ventana abierta mientras trabajas con MongoDB
- Si la PC se reinicia, se debe de volver a iniciar el servidor

5. En el mismo directorio del paso 4 ejecuta el instalador de compass con el siguiente comando:

$ powershell -ExecutionPolicy Bypass -File Install-Compass.ps1

Lo cual iniciará la descarga e instalación de MongoDBCompass

6. Una vez instalado se abrirá la herramienta Compass, presione el botón start y luego “add new connection” y se abrirá una ventana como la siguiente en donde solo debe colocar el Nombre y si lo desea un color, luego presiona “Save and Connect”
7. Al costado izquierdo de la pantalla aparecerá el servidor al que nos acabamos de conectar
8.Para crear una nueva base de datos presione el botón “+” que aparece junto al nombre del servidor al que nos acabamos de conectar, deberá aparecer una ventana en la cual solo deberán de colocar el nombre de la base de datos y el de la colección, para finalizar se debe presionar el botón “Create Database”
9. Para poblar la base de datos se va a utilizar un archivo .csv el cual contiene 10 000 registros de usuarios, donde cada usuario tendrá un nombre de usuario, un identificador de región, primer nombre, teléfono, correo electrónico y fecha de nacimiento.
10. Una vez se tiene el csv listo para la población, se procede a realizar la inserción de los datos desde MongoDBCompass, se debe ubicar en la colección donde se desean agregar estos datos y presionar el botón verde que dice “Add Data” y seguidamente la opción de “import JSON or CSV file”.
Una vez seleccionado esto, se abrirá un explorador de archivos para seleccionar nuestro csv.

11. Una vez seleccionado el documento, MongoDBCompass detectará automáticamente cada elemento que queremos insertar y nos mostrará una ventana emergente con algunas opciones adicionales, donde podemos elegir el delimitador e incluso el tipo de dato de cada atributo. Luego solo se debe presionar el botón “Import” para realizar la inserción.
12. Al terminar el paso anterior, se muestra un mensaje de éxito y ya podemos ver los documentos insertados.

CONFIGURACION DE REDIS.
1. Ejecutar en la terminal de Ubuntu los siguientes comandos

sudo apt update
sudo apt upgrade
sudo apt install redis-server
sudo snap install code --classic
sudo apt install python3
sudo apt install python3-redis

2. Abrir el IDE (Visual Studio Code en este caso), para ejecutar las siguientes lineas

import redis
import time

r = redis.Redis(host='localhost', port=6379, db=0)

A partir de ahi se pueden hacer todos los sets o gets necesarios segun el codigo.
