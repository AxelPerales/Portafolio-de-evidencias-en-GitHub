# ERNESTO JESUS CANO ARENAS
# AXEL MANUEL PERALES TEOFILO


import subprocess
import argparse

# Argumentos
info = '''Programa encriptador de archivos
nota: el uso actual es de un solo archivo, no se aceptan carpetas
-------Ejemplo de uso---------
-En el caso de querer encriptar un archivo de la carpeta actual se puede usar el path relativo
python Encrypt.py -file "./Ejemplo.txt"

-En el caso de encriptar un objeto de otra carpeta utilizar el path absoluto
python Encrypt.py -file "C:/Users/Anonimo/Desktop/mystery_img1.jpg" 
''' 

parser = argparse.ArgumentParser(description ="Encriptar archivos",
                                epilog = info,
                                formatter_class = argparse.RawDescriptionHelpFormatter)
parser.add_argument("-file", metavar="FILE", dest="file", help="Archivo a encriptar",required=True)

param = parser.parse_args()

file = param.file

# Ejecucion
try:
    comando = "./Encriptador.ps1 -file " + file 
    lineaPS = "powershell -ExecutionPolicy ByPass -Command " + comando
    #print(file)
    #print(comando)
    #print(lineaPS)
    runningProcesses = subprocess.check_output(lineaPS)
    print(runningProcesses.decode())
except Exception as e:
    print(str(e))
