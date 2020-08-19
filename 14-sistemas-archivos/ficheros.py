from io import open
import pathlib

#Abrir archivo

ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"#Esto devuelve la ruta donde se encuentra el archivo
print(ruta)
archivo = open(ruta, "a+")

# Escribir 
archivo.write("Soy un texto")

# Cerrar archivo
archivo.close