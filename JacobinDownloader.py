
import os
import requests

# saving url constants for magazine's url / Partes fijas de la url

URL_1='https://jacobinlat.com/wp-content/uploads'
URL_2='revista-Jacobin_No'
URL_3='_ed-digital.pdf'

# User's input for url's variable parts / Input de usuario para partes variables de la url

YEAR=input("ingrese año de edicion / input edition's year: ")
MONTH=input("ingrese mes de edicion / input edition's  month: ")
NMB=input("Ingrese numero de edicion/ input edition's number: ")

# String concatenation for url crafting / Concatenacion para formar la url final.

URL= URL_1 + '/' + YEAR + '/' + MONTH + '/' + URL_2 + NMB + URL_3
print('URL:', URL)

# Requesting the crafted url / Peticion http de la url obtenida

RQT=requests.get(URL)
CODE=RQT.status_code

# Write the directory  you want to save at / Eleccion de directorio de descarga

DIR="" 
print("Directorio de guardado/Save directory: " + DIR)

# If http status code = 200 the url is valid and we proceed to search or create the save directory 
# Si el codigo de estado http es 200, la url es valida y procedemos a buscar o crear el directorio de descarga
# then we download the magazine. 
# Luego descargamos la revista
# If status code is not 200 then the url is not valid and we throw an error message.
# Si el codigo de estado no es 200, entonces la url no es valida y mostramos un mensaje de error

if CODE == 200: 
    if not os.path.exists(DIR):
        os.makedirs(DIR)
    pdf = open(DIR + '/' + 'jacobin' + NMB + '.pdf', 'wb')
    pdf.write(RQT.content)
    pdf.close()
    print("Archivo descargado / File downloaded")
else:       
    print('URL invalida / Invalid URL')    
