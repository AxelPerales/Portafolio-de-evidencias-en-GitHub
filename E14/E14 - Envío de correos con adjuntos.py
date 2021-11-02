#E14-Envios de correos con adjuntos
#Axel Manuel Perales Teófilo
#Ernesto Jesús Cano Arenas

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import smtplib
import getpass
import os


#Variables del entorno
print("Ingresa tus datos. ")
user = input("Ingresa tu correo electronico: ") #
password = getpass.getpass("Ingresa tu contraseña de correo: ")#

#cabezara del email
remitente = ("From, De: $user ")
destinatario = input("To, Para: ") #
asunto = input("Subject, Asunto: ")
mensaje = input("Mensaje: ")
archivo = input("Ruta del archivo: ")

#conexion SMTP
conexion = smtplib.SMTP('smtp.gmail.com', port= 587)

#Encriptador TLS
conexion.starttls()

#Iniciar sesión en el SMTP
conexion.login(user, password)

#Depuración de envio
conexion.set_debuglevel(1)

header =  MIMEMultipart()
header ['Subject'] = asunto
header["From"] = remitente
header['To'] = destinatario

mensaje = MIMEText(mensaje, 'plain') #Content -type: text/plain
header.attach(mensaje)

if (os.path.isfile(archivo)):
    adjunto = MIMEBase('application', 'octet-stream')
    adjunto.set_payload(open(archivo, "rb").read())
    encode_base64(adjunto)
    adjunto.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(archivo))
    header.attach(adjunto)


#Envio de correo
conexion.sendmail(remitente, destinatario, header.as_string())

#Desconectar del servidor
conexion.quit()
