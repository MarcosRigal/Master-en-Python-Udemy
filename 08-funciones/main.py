"""
def nombreDeMiFunción(parametros)
  #bloque / conjunto de instrucciones
"""

print("##### Ejemplo 1####")

def muestraNombre():
  print("Victor")
  print("Paco")
  print("Marcos")

# Invocar función

muestraNombre()
muestraNombre()

# Ejemplo 2

print("##### Ejemplo 2####")

def mostrarTuNombre(nombre, edad):
  print(f"Tu nombre es: {nombre}")
  if(edad >= 18):
    print("Eres mayor de edad")

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
mostrarTuNombre(nombre, edad)

# Ejemplo 3

print("##### Ejemplo 3####")

def tabla(numero):
  for contador in range(1,11):
    print(f"{numero} x {contador} = {numero * contador}")

tabla(3)

for numero_tabla in range(1, 11):
  tabla(numero_tabla)

# Ejemplo 4

print("##### Ejemplo 4####")

# Parámetros opcionales

def getEmpleado(nombre, dni = None):
  print(nombre)
  if dni != None:
    print(dni)

getEmpleado("Marcos", 32731909)

# Ejemplo 5

print("##### Ejemplo 5####")

# Return o devolver datos

def saludame(nombre):
  saludo = f"Hola, saludos {nombre}"
  return saludo

print(saludame("Marcos"))

# Ejemplo 6

print("##### Ejemplo 6####")

def calculadora(n1, n2, basicas = False):
  
  suma = n1 + n2
  resta = n1 - n2
  multi = n1 * n2
  div = n1 / n2

  cadena = ""
  if basicas != False:
    cadena += "Suma:" + str(suma)
    cadena += "Resta: " + str(resta)

  else:
    cadena += "Producto: " + str(multi)
    cadena += "Division: " + str(div)
  
  return cadena
  

print(calculadora(56, 5))

# Ejemplo 7

print("##### Ejemplo 7####")

def getNombre(nombre):
  texto = f"El nombre es: {nombre}"
  return texto

def getApellidos(apellidos):
  texto = f"Los apellidos son: {apellidos}"
  return texto

def devuelveTodo(nombre, apellidos):
  texto = getNombre(nombre) + "\n" + getApellidos(apellidos) 
  return texto

print(devuelveTodo("Marcos", "Rivera"))

# Ejemplo 8: Funciones Lamda

# Son funciones que se definen en una única linea y que se utilizan para cosas muy concretas

print("##### Ejemplo 8####")

year = lambda año: f"El año es {año}"

print(year(2034))