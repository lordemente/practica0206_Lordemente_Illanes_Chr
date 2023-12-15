def x(n):
    '''Escribir una función que pida un número entero entre 1 y 10 y guarde
    en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese
    número, donde n es el número introducido.'''
    if n > 0 and n <= 10: 
        with open(f"C:\\Users\\CHRISTO\\OneDrive\\Escritorio\\"
                f"Illanes_Christopher_Examen_DAPI_UT2_2M\\"
                f"Illanes_Christopher_Examen_DAPI_UT2_2M\\"
                f"Ficherosssss\\tabla-{n}.txt","w") as fichero:
            for i in range(1,11):
                multiplicar = n * i    
                
                fichero.write(f"{n} * {i} = {multiplicar}\n")

            print("fichero creado")
    else:
        print("Fichero no creado")

for i in range(1,12):

    a = int(input("entre el 1 al 10: "))


    x(a)