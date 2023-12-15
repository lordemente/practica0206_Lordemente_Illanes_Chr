import urllib.request


'''Escribir un programa que acceda al fichero de internet mediante la url
 indicada y muestre por pantalla el número de palabras que contiene.'''


def url(variabluURL):
    archivo = urllib.request.urlopen(variabluURL)
   
    for i in archivo:
        decodificador = i.decode("utf-8")
        print(decodificador)
    longitud = len(decodificador)
    return f"Longitud del texto: {longitud}"




x = "http://textfiles.com/adventure/aencounter.txt"
print(url(x))