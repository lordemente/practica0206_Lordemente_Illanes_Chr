import os
def lectura(n):
    '''Escribir una función que pida un número entero entre 1 y 10, lea el
    fichero tabla-n.txt con la tabla de multiplicar de ese número, donde n
    es el número introducido, y la muestre por pantalla. Si el fichero no
    existe debe mostrar un mensaje por pantalla informando de ello.'''
    if n > 0 and n <= 10:
       
        if os.path.isfile(f"C:\\Users\\CHRISTO\\OneDrive\\Escritorio\\"
                f"Illanes_Christopher_Examen_DAPI_UT2_2M\\"
                f"Illanes_Christopher_Examen_DAPI_UT2_2M\\"
                f"Ficherosssss\\tabla-{n}.txt"):
            with open(f"C:\\Users\\CHRISTO\\OneDrive\\Escritorio\\"
                f"Illanes_Christopher_Examen_DAPI_UT2_2M\\"
                f"Illanes_Christopher_Examen_DAPI_UT2_2M\\"
                f"Ficherosssss\\tabla-{n}.txt","r") as file:
                print(file.read())
        else:
            print("El fichero no existe")


contador = 0
while contador <= 3:
    usuario = int(input("Ingresa un número entre el 1 al 10: "))
    lectura(usuario)
    contador += 1