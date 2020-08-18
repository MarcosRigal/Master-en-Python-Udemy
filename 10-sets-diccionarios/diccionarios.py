"""

Un diccionario es un tipo de dato que almacena otros conjuntos de datos en formato:
clave > valor (Es como un struct)

"""

persona = {
  "nombre": "Marcos",
  "apellidos": "Rivera",
  "correo": "riveragavilanmarcos@gmail.com"
}

print(persona["correo"])

# Lista con diccionarios (Array de Structs)

contactos = [
  {
    "nombre": "Marcos",
    "email": "marcosrigal@gmail.com"
  },
  {
    "nombre": "Pepe",
    "email": "pepe@gmail.com"
  },
  {
    "nombre": "Salva",
    "email": "salvador@gmail.com",
  }
]

print(contactos[0]["nombre"])

print("\n Listado de contactos: ")
print("----------------------")
for contacto in contactos:
  print(f"Nombre del contacto: {contacto['nombre']}")
  print(f"Email del contacto: {contacto['email']}")
  print("----------------------")