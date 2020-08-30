from coche import Coche

carro = Coche("Amarillo", "Seat", "Panda", 250, 150, 5)
carro1 = Coche("Verde", "Citröen", "Picassa", 200, 96, 7)
carro2 = Coche("Azul", "Seat", "Ibiza", 200, 100, 5)
carro3 = Coche("Rojo", "Mercedes", "GLA", 300, 400, 2)

print(carro.getColor())

print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

# Detectar tipado

if isinstance(carro3, Coche):
  print("Es un dato correcto.")
else:
  print("No es un dato correcto")

"""
Visibilidad: podemos distinguir entre clases publicas y clases privadas.
Hasta ahora hemos definido clases públicas.
Para definir clases privadas antes del nombre debemos poner __
"""

print(carro.soy_publico)
print(carro.getPrivado())