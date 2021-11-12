#E15-Pyautogui
#Axel Manuel Perales Teófilo
#Ernesto Jesús Cano Arenas
from faker import Faker
import pyautogui
import time

fr1 = input("Frase para primer llenado: ")
fr2 = input("Frase para segundo llenado: ")

faker = Faker()
em = faker.email()
em2 = faker.email()

datos = [{'opcion': 'Ambos', 'frase': fr1, 'hora': '11', 'correo': em},
            {'opcion': 'Marvel', 'frase': fr2, 'hora': '10', 'correo': em2},
            ]

for vuelta in datos:
    time.sleep(5)
    if vuelta['opcion'] == 'Ambos':
        pyautogui.click(x = 256, y = 632, clicks = 1)
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('tab')
    elif vuelta['opcion'] == 'Marvel':
        pyautogui.click(x = 253, y = 533, clicks = 1)
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('tab')
        
    pyautogui.typewrite(vuelta['frase'])
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    if vuelta['hora'] == '11':
        pyautogui.press('enter')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('tab')  
    elif vuelta['hora'] == '10':
        pyautogui.press('enter')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('tab')  

    pyautogui.typewrite(vuelta['correo'])
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.click(x = 316, y = 486 , clicks = 1)
