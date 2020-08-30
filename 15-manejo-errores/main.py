"""
# Capturar excepciones y manejar errores en código
# susceptible a fallos/errores

try:#Comprueba el funcionamiento
  nombre = input("¿Cual es tu nombre?")
  if len(nombre) > 1:
    nombre_usuario = "El nombre es: " + nombre

  print(nombre_usuario)
except:#Si va mal
  print("Ha ocurrido un error, introduzca un nombre válido")
else:
  print("Todo ha ido bien")# Si va bien 
finally:
  print("Fin de la iteración")#Siempre
"""
#Multiples excepciones
try:
  numero = int(input("Introduce un numero para elevarlo al cuadrado:"))
  print(f"El cuadrado es: {numero * numero}")
except TypeError:
  print("Debes convertir tus cadenas a enteros en el codigo")
except ValueError:
  print("Introduce un numero correcto")
except Exception as e:
  print(type(e))
  print(f"Ha ocurrido un error: {type(e).__name__}")

# Exceociones personalizadas o lanzar excepcion
try:
  nombre = input("Introduce el nombre: ")
  edad = int(input("Introduce la edad: "))

  if edad < 5 or edad >110:
    raise ValueError("La edad introducida no es real")
  elif len(nombre) <= 1:
    raise ValueError("El nombre no esta completo")
  else:
    print("Hola")
except ValueError:
  print("Introduce los datos correctamente")
except Exception as e:
  print(f"Existe un error: {e}")