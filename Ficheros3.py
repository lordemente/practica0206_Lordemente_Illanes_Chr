def lectura(n,m):
    '''Escribir una función que pida dos números n y m entre 1 y 10,
    lea el fichero tabla-n.txt con la tabla de multiplicar de ese número,
    y muestre por pantalla la '''
   
    if m > 0 and m <= 10:
        with open(f"C:\\Users\\CHRISTO\\OneDrive\\Escritorio\\"
                f"Illanes_Christopher_Examen_DAPI_UT2_2M\\"
                f"Illanes_Christopher_Examen_DAPI_UT2_2M\\"
                f"Ficherosssss\\tabla-{n}.txt","r") as leer:
            lista = leer.readlines()
            for i in lista:
                linea = lista[m]
            print(F"Linea Nº {m}: {linea}")
       
       
    else:
        return f"No existe el fichero: tabla-{n}"
   


n = int(input("Ingresa un número entre el 1 y el 10: "))
m = int(input("Ingresa un número entre el 1 y el 10: "))
lectura(n,m)