nombre = "Marcos"

# Funciones generales

print(type(nombre))

# Detectar el tipado

comprobar = isinstance(nombre, str)
if comprobar: #Si no le ponemos operador de comparacion el if "entiende" que queremos que sea true
  print("Esa variable es un string")

else: 
  print("No es una cadena")

if not isinstance(nombre, float):
  print("La variable no es un numero con decimales")

# Limpiar espacios

frase = "     mi espacio     "
print(frase)
print(frase.strip()) #.strip es un metodo que elimina los espacios a los lados

# Eliminar variables

year = 2022
print(year)
del year #Del elimina la variable

# Comprobar variable vacía

texto = "  ff  "

if len(texto) <= 0: # len devuelve un entero correspondiente al numero de caracteres de la cadena
  print("La variable esta vacia")
else: 
  print("La variable tiene contenido: ", len(texto))

# Econtrar 
