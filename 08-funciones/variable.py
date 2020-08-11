"""
Variables locales: Se definen dentro de la funcion yno se puede usar fuera de ella,
solo estan disponibles dentro a no ser que hagamos un return.

Variables globales: Son las que se declaran fuera de una duncion y estan disponibles
dentro y fuera de ellas.
"""

# Variable global:

frase = "Hola a todos"
print(frase)

def hola():
  frase = "Hola mundo!!"
  print("Dentro de la función: ")
  print(frase)

  global year
  year = 2021
  print(year)

  return "Dato devuelto " + str(year)

print(hola())
print(year)