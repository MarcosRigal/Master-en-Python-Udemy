"""
Listas (arrays)
Son colecciones o conjuntos de datos/valores, bajo un unico nombre.
Para acceder a esos valores podemos usar un indice numérico
"""

# Definir lista
peliculas = ["Batman", "Spiderman", "El señor de los anillos"]
cantantes = list(('Hola', 'me','llamo Marcos'))#En realidad le pasas una tupla y la convierte en lista por eso los dos parentesis
year = list(range(2020,2050))
plato_combinado = ["Marcos", 5, False, 6.9]

print(peliculas)
print(cantantes)
print(year)
print(plato_combinado)

# Indices

print(peliculas[1])
peliculas[1:] = "cars", "BBQ", "Planes"
print(peliculas[-2])#Imprime lo mismo que el de arriba porque empieza desde el ultimo
print(cantantes[0:2])# Imprime la sublista que va del 0 al 2 (solo imprime 0 y 1 el dos se queda fuera)
print(peliculas[1:])# Imprime todos los que hay desde ese

print(peliculas[:2])# Imprime todos los que hay hasta ese

# Añadir elemento a lista
cantantes.append("Sabaton")
print(cantantes)

# Recorrer lista
print("***** Listado peliculas ******")
for pelicula in peliculas:
  print(f"{peliculas.index(pelicula)}.{pelicula}") #.index devuelve el indice dentro de la lista del elemento


# Listas multidimensionales ¿Matrices?

contactos = [
  [
    "Antonio",
    "antonio@gmail.com"
  ],
  [
    "Marcos",
    "marcos@gmail.com"
  ],
  [
    "Calvo",
    "calvo@gmail.com"
  ]
]

for contacto in contactos:
  for elemento in contacto:
    if contacto.index(elemento) == 0:
      print(f"Nombre: {elemento}")
    else:
      print(f"Correo: {elemento}")
  print("\n")

print(contactos[0])