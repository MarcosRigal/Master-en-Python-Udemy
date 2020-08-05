"""
# for

for variable in elemento_iterable (lista, rango, etc)
  BLOQUE DE INSTRUCCIONES
  break hace que salgas del bucle

"""

contador = 0
resultado = 0

for contador in range(0,5):
  print(f"Voy por el {contador}")
  resultado += contador

print(f"El resultado es {resultado}")

# Ejemplo tablas de multiplicar

numero = int(input("¿De que número quieres ver la tabla?: "))

for numero_tabla in range(1,11):
  print(numero_tabla*numero)
#else: texto (se ejecuta cuando acaba el bucle si no se ha salido con un break)