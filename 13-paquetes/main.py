#Cuando crees un paquete tienes que crear el archivo _init_.py vacio y luego un archivo para cada modulo.
#Un paquete es un conjunto de modulos

print("PROBANDO PAQUETES")

from mipaquete import pruebas
from mipaquete import herramientas

pruebas.probando()
herramientas.nombreCompleto("Marcos", "Rivera")