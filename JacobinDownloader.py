
import os
import requests
URL_1='https://jacobinlat.com/wp-content/uploads'
URL_2='revista-Jacobin_No'
URL_3='_ed-digital.pdf'
YEAR=input("ingrese año de edicion / input edition's year: ")
MONTH=input("ingrese mes de edicion / input edition's  month: ")
NMB=input("Ingrese numero de edicion/ input edition's number: ")
URL= URL_1 + '/' + YEAR + '/' + MONTH + '/' + URL_2 + NMB + URL_3
print('URL:', URL)
R=requests.get(URL)
CODE=R.status_code
DIR="" #Write the directory  you want to save at
print("Directorio de guardado/Save directory: " + DIR)
if CODE == 200:
    if not os.path.exists(DIR):
        os.makedirs(DIR)
    pdf = open(DIR + '/' + 'jacobin' + NMB + '.pdf', 'wb')
    pdf.write(R.content)
    pdf.close()
    print("Archivo descargado / File downloaded")
else:       
    print('URL invalida / Invalid URL')    
