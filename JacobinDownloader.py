
import os
import requests

# saving url constants for magazine's url

URL_1='https://jacobinlat.com/wp-content/uploads'
URL_2='revista-Jacobin_No'
URL_3='_ed-digital.pdf'

# User's input for url's variable parts

YEAR=input("ingrese año de edicion / input edition's year: ")
MONTH=input("ingrese mes de edicion / input edition's  month: ")
NMB=input("Ingrese numero de edicion/ input edition's number: ")

# String concatenation for url crafting 

URL= URL_1 + '/' + YEAR + '/' + MONTH + '/' + URL_2 + NMB + URL_3
print('URL:', URL)

# Requesting the crafted url

R=requests.get(URL)
CODE=R.status_code

#Write the directory  you want to save at

DIR="" 
print("Directorio de guardado/Save directory: " + DIR)

#If http status code = 200 the url is valid and we proceed to search or create the save directory, then we download the magazine. If status code is not 200 then the url is not valid and we throw an error message.
    
if CODE == 200: 
    if not os.path.exists(DIR):
        os.makedirs(DIR)
    pdf = open(DIR + '/' + 'jacobin' + NMB + '.pdf', 'wb')
    pdf.write(R.content)
    pdf.close()
    print("Archivo descargado / File downloaded")
else:       
    print('URL invalida / Invalid URL')    
