# ERNESTO JESUS CANO ARENAS
# AXEL MANUEL PERALES TEOFILO


# Requerimientos
# Tener los 2 scripts en la misma carpeta (Modulos.py E12.py) y el archivo "dictEsp.txt"

# Importaciones
import argparse
import Modulos


# Argumentos para ejecucion
info = '''Script para encriptacion, desencriptar y crackear cifrado cesar
+Ejemplo de uso:
E12.py -modo e -mensaje "Mensaje de ejemplo"
E12.py -modo e -mensaje "Mensaje de ejemplo" -clave "Clave generica"'''

parser = argparse.ArgumentParser(description='E12',
                               epilog=info,
                            formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-modo", metavar="Modo", dest="modo",
                    help="""Accion que se le realizara al mensaje
                    Modos disponibles:
                    e : encriptar
                    d : desencriptar
                    c : crackear""", required=True)
parser.add_argument("-mensaje", metavar="Mensaje",dest="mensaje",
                help="Mensaje que se encriptara/desencriptara/crackeara",
                required=True)                    
parser.add_argument("-clave", metavar="Clave",dest="clave",
                help="clave para encriptar/desencriptar mensaje",
                required= False)

params = parser.parse_args()
modo = params.modo
mensaje = params.mensaje
clave = params.clave

# Ejecucion
if modo == "e":
    espacios = 1    
    if clave is None:
        clave = "prueba" 
    while espacios > 0:
        espacios = clave.count(" ")
        if clave.isalpha() == False:
            espacios += 1
    key = len(clave)
    print("modo: ",modo,"\t","mensaje: ", mensaje,"\t","clave usada: ", clave )
    Modulos.cifrar(mensaje, key)

elif modo == "d":
    espacios = 1
    if clave is None:
        clave = "prueba" 
    while espacios > 0:
        espacios = clave.count(" ")
        if clave.isalpha() == False:
            espacios += 1
    key = len(clave)
    print("modo: ",modo,"\t","mensaje: ", mensaje,"\t","clave usada: ", clave )   
    Modulos.descifrar(mensaje, key)

elif modo == "c":
    Modulos.crackeo(mensaje)

elif modo != "c":
    print("Error modo: ",modo," no es una opcion disponible")