#Axel Manuel Perales Teofilo
#Metadata de imágenes en la web
#E11
import requests
import os
import argparse
from bs4 import BeautifulSoup
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image

parser = argparse.ArgumentParser(description='Metadatos en imágenes de la web.',
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-link', metavar='LINK', dest="link", 
                    help="URL")
params = parser.parse_args()

def scrapingBeautifulSoup(url):
    try:
        print("Obteniendo imagenes con BeautifulSoup "+ url)
            
        response = requests.get(url)
        bs = BeautifulSoup(response.text, 'lxml')
            
        #create directory for save images
        os.system("mkdir images")
            
        for tagImage in bs.find_all("img"): 
            #print(tagImage['src'])
            if tagImage['src'].startswith("http") == False:
                download = url + tagImage['src']
            else:
                download = tagImage['src']
            print(download)
            # download images in img directory
            r = requests.get(download)
            f = open('images/%s' % download.split('/')[-1], 'wb')
            f.write(r.content)
            f.close()
        
    except Exception as e:
            print(e)
            print("Error conexion " + url)
            pass

        
def decode_gps_info(exif):
    gpsinfo = {}
    if 'GPSInfo' in exif:
        #Parse geo references.
        Nsec = exif['GPSInfo'][2][2] 
        Nmin = exif['GPSInfo'][2][1]
        Ndeg = exif['GPSInfo'][2][0]
        Wsec = exif['GPSInfo'][4][2]
        Wmin = exif['GPSInfo'][4][1]
        Wdeg = exif['GPSInfo'][4][0]
        if exif['GPSInfo'][1] == 'N':
            Nmult = 1
        else:
            Nmult = -1
        if exif['GPSInfo'][1] == 'E':
            Wmult = 1
        else:
            Wmult = -1
        Lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
        Lng = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)
        exif['GPSInfo'] = {"Lat" : Lat, "Lng" : Lng}
        input()

def get_exif_metadata(image_path):
    ret = {}
    image = Image.open(image_path)
    if hasattr(image, '_getexif'):
        exifinfo = image._getexif()
        if exifinfo is not None:
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)
                ret[decoded] = value
    decode_gps_info(ret)
    return ret

def guardar_meta(name, meta, ruta):
    filename = ruta + "/metadata__" + name + ".txt"
    f.open(filename, "w")
    i=0
    for i in meta:
        f.write(i)
        f.write("\n")
        f.close
        
def printMeta():
    os.chdir("imagenes")
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            print(os.path.join(root, name))
            print ("[+] Metadata for file: %s " %(name))
            input()
            try:
                exifData = {}
                exif = get_exif_metadata(name)
                for metadata in exif:
                    meta.append("Metadata: %s - Value: %s " %(metadata, exif[metadata]))
                    save_meta(name, meta, ruta)
                    file = open(name+".txt","a")
                    print ("Metadata: %s - Value: %s " %(metadata, exif[metadata]))
                    file.write("Metadata: %s - Value: %s " %(metadata, exif[metadata]))
                    file.write("\n")
                    file.close
                print ("\n")
                decode_gps_info(exif)
            except:
                import sys, traceback
                traceback.print_exc(file=sys.stdout)


if __name__ == "__main__":
    if params.link != None:
        scrapingBeautifulSoup(params.link)
        printMeta()
    

