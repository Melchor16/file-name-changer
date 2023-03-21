import os
from datetime import datetime
from pathlib import Path

def main():
    global fpath
    fpath = Ruta()
    lista_archivos = os.listdir(fpath)

    print('\n1. Replace part of the name.')
    print('2. Add a prefix and/or suffix.')
    print('3. Rename all files with a consecutive number.')
    print('4. Order files by creation date and rename all with a consecutive number.')
    
    opcion = int(input('\nChoose an option and write the number: '))

    while opcion > 4 or opcion < 1:
        opcion = int(input('Invalid opcion, please select a valid option: '))
    
    if opcion == 1:  #OPCION 1
        buscar = input('Text to replace: ')
        reemplazo = input('Replace with: ')
        extension = input('Extension of files to rename (empty for all): ')

        omi = ReemplazarTexto(lista_archivos, buscar, reemplazo, extension)

        print('\nDone!\n')
    
        if len(omi)>0:
            print('This file names already exists:')
            for i in omi:
                print(i)
            print('\n')
        
        else:
            print('No omissions found.\n')

        z=input('Press ENTER to exit.')

    elif opcion == 2: #OPCION 2
        sufijo = input('Write a suffix (Enter to skip): ')
        prefijo = input('Write a prefix (Enter to skip): ')
        extension = input('Extension of files to rename (empty for all): ')
        omi = SufijoPrefijo(lista_archivos, sufijo, prefijo, extension)

        print('\nDone!\n')
    
        if len(omi)>0:
            print('This file names already exists:')
            for i in omi:
                print(i)
            print('\n')
        
        else:
            print('No omissions found.\n')

        z=input('Press ENTER to exit.')
           
    elif opcion == 3: #OPCION 3
        constante = input('Write a constant: ')
        numero_digitos = int(input('Number of digits of the consecutive (max 5): '))
        while numero_digitos>5 or numero_digitos<1:
            print('ERROR: Number of digits must be between 1 and 5.')
            numero_digitos = int(input('Number of digits of the consecutive (max 5): '))
        numero_digitos-=1
        extension = input('Extension of files to rename (empty for all): ')

        Consecutivo(lista_archivos, constante, extension, numero_digitos)

        print('\Done!\n')

        z=input('Press ENTER to exit.')

    elif opcion == 4: #OPCION 4
        
        ordenados = sorted(Path(fpath).iterdir(), key=os.path.getctime)
        ordenados_str =[]
        for i in ordenados:
            ordenados_str.append(str(i))

        constante = input('Write a constant: ')
        numero_digitos = int(input('Number of digits of the consecutive (max 5): '))
        while numero_digitos>5 or numero_digitos<1:
            print('ERROR: Number of digits must be between 1 and 5.')
            numero_digitos = int(input('Number of digits of the consecutive (max 5): '))
        numero_digitos-=1
        extension = input('Extension of files to rename (empty for all): ')

        Creacion(ordenados_str, constante, extension, numero_digitos)

        print('\Done!\n')

        z=input('Press ENTER to exit.')


def Ruta():
    ruta_existe = False
    while ruta_existe == False:
        carpeta = input('Folder Path: ')
        if os.path.exists(carpeta) == True:
            ruta_existe=True
        else:
            print('ERROR: Path not found.')
    return carpeta

def Repetidos(lista, nombre):
    omisiones = ''
    repetido = False
    for comparacion in lista:
        if comparacion == nombre:
            repetido = True
            omisiones = nombre
    return omisiones

def ReemplazarTexto(archivos, reemplazar, con, ext):
    omisiones = []
    for nombre in archivos:
        if nombre.find(reemplazar)>=0 and nombre.find(ext)>=0:
            nuevo = nombre.replace(reemplazar, con)
            nuevo_completo = fpath + '\\' + nuevo
            antiguo_completo = fpath + '\\' + nombre
            
            rep = Repetidos(archivos, nuevo)    

            if len(rep) > 0:
                omisiones.append(rep)
                continue
            else:
                os.rename(antiguo_completo, nuevo_completo)
    
    return omisiones

def SufijoPrefijo(archivos, suf, pref, ext):
    omisiones = []
    for nombre in archivos:
        if nombre.find(ext)>=0:
            for letra in range(len(nombre)):
                if nombre[letra] == '.':
                    clave = letra
            
            nombre_nuevo = pref + nombre[:clave] + suf + nombre[clave:]
            nombre_nuevo_completo = fpath + '\\' + nombre_nuevo
            nombre_antiguo = fpath + '\\' + nombre

            rep = Repetidos(archivos, nombre_nuevo)    

            if len(rep) > 0:
                omisiones.append(rep)
                continue
            else:
                os.rename(nombre_antiguo, nombre_nuevo_completo)

    return omisiones

def Consecutivo(archivos, const, ext, dig):
    omisiones = []
    consecutivo = 1
    for nombre in archivos:
        for letra in range(len(nombre)):
            if nombre[letra] == '.':
                clave = letra

        if nombre.find(ext)>=0:

            if consecutivo <10:
                nombre_nuevo = const + '0'*dig + str(consecutivo) + nombre[clave:]
            
            elif consecutivo >=10 and consecutivo <100:
                nombre_nuevo = const + '0'*(dig-1) + str(consecutivo) + nombre[clave:]
            
            elif consecutivo >=100 and consecutivo <1000:
                nombre_nuevo = const + '0'*(dig-2) + str(consecutivo) + nombre[clave:]
            
            elif consecutivo >=1000 and consecutivo <10000:
                nombre_nuevo = const + '0'*(dig-3) + str(consecutivo) + nombre[clave:]
            
            else:
                nombre_nuevo = const + str(consecutivo) + nombre[clave:]


            nombre_nuevo_completo = fpath + '\\' + nombre_nuevo
            nombre_antiguo = fpath + '\\' + nombre
            
            rep = Repetidos(archivos, nombre_nuevo)    

            if len(rep) > 0:
                omisiones.append(rep)
                continue
            else:
                os.rename(nombre_antiguo, nombre_nuevo_completo)
                consecutivo += 1
        
def Creacion(archivos, const, ext, dig):
    omisiones = []
    consecutivo = 1
    for nombre in archivos:
        for letra in range(len(nombre)):
            if nombre[letra] == '.':
                clave = letra

        if nombre.find(ext)>=0:

            if consecutivo <10:
                nombre_nuevo = const + '0'*dig + str(consecutivo) + nombre[clave:]
            
            elif consecutivo >=10 and consecutivo <100:
                nombre_nuevo = const + '0'*(dig-1) + str(consecutivo) + nombre[clave:]
            
            elif consecutivo >=100 and consecutivo <1000:
                nombre_nuevo = const + '0'*(dig-2) + str(consecutivo) + nombre[clave:]
            
            elif consecutivo >=1000 and consecutivo <10000:
                nombre_nuevo = const + '0'*(dig-3) + str(consecutivo) + nombre[clave:]
            
            else:
                nombre_nuevo = const + str(consecutivo) + nombre[clave:]


            nombre_nuevo_completo = fpath + '\\' + nombre_nuevo
            nombre_antiguo = fpath + '\\' + nombre
            
            rep = Repetidos(archivos, nombre_nuevo)    

            if len(rep) > 0:
                omisiones.append(rep)
                continue
            else:
                os.rename(nombre, nombre_nuevo_completo)
                consecutivo += 1
            



if __name__ == "__main__":
    main()