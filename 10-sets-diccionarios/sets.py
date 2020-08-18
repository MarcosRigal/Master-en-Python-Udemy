"""
Set es un tipo de dato, para tener una coleccion de valores, 
pero no tiene ni indice ni orden

Es un conjunto en el que no puede haber elementos repetidos
"""

personas ={
  "Victor", "Manolo", "Marcos"
}

personas.add("Paco")
personas.remove("Marcos")

print(type(personas))
print(personas)