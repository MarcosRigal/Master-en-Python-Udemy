import os #Necesario para trabajar con directorios
import shutil # Necesario para copiar y pegar

# Crear carpeta

if not os.path.isdir("./mi_carpeta"):
  os.mkdir("./mi_carpeta")
else:
  print("Ya existe el directorio")

# Eliminar carpeta
"""
os.rmdir("./mi_carpeta")
"""

# Copiar carpeta
ruta_original = "./mi_carpeta"
ruta_copiada = "./mi_carpeta_COPIADA"
"""
shutil.copytree(ruta_original, ruta_copiada)
"""
print("Contenido de mi carpeta:")
contenido = os.listdir(ruta_original)
for fichero in contenido:
  print(f"Fichero: {fichero}")
