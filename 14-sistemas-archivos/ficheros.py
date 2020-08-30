from io import open #para trabajar con archivos
import shutil #copiar y borrar archivos

# Abrir archivo
ruta =  "14-sistemas-archivos/fichero_texto.txt"
archivo = open(ruta, "a+")

# Escribir
archivo.write("Soy un texto\n")

# Cerrar archivo
archivo.close()

ruta =  "14-sistemas-archivos/fichero_texto.txt"
archivo_lectura = open(ruta, "r")
"""
# Leer contenido
contenido = archivo_lectura.read()

print(contenido)
"""

# Leer contenido y guardarlo en una lista
lista = archivo_lectura.readlines()
archivo_lectura.close

print(lista)

for frase in lista:
  print("-" + frase)

ruta_original = "14-sistemas-archivos/fichero_texto.txt"
ruta_nueva = "14-sistemas-archivos/fichero_texto_copiado.txt"
"""
# Copiar
shutil.copyfile(ruta_original, ruta_nueva)

# Mover

shutil.move(ruta_original, ruta_nueva)

# Eliminar
import os
os.remove(ruta_nueva)
"""
# Comprobar si existe 
import os.path

if os.path.isfile(ruta_original):
  print("Existe")
if os.path.isfile(ruta_nueva):
  print("Existe")