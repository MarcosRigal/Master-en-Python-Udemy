"""
Módulos: son funcionalidades ya hechas para reutilizar.

En python hay muchos modulos, se pueden consultar en:
https://docs.python.org/es/3/py-modindex.html

Podemos conseguir modulos que ya vienen en el lenguaje,
modulos en internet, y tambien podemos crear nuestros modulos.
"""

# Importar modulo propio
"""
import mimodulo

print(mimodulo.holaMundo("Marcos")) #Así importas todas las funciones

print(mimodulo.calculadora(3,5,True))
"""

from mimodulo import holaMundo
                                #Así solo importas una función
print(holaMundo("Marcos"))

"""
Si quieres importarlo todo sin tener que poner delante mi modulo puedes hacer:
from mimodulo import * 
"""

# Modulo Fechas

import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now() #Devuelve un objeto con propiedades

print(fecha_completa) 
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)
print(fecha_completa.time())

# Para dar formato nos fijamos en la documentacion

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H/%M/%S")
print(fecha_personalizada)
print(datetime.datetime.now().timestamp())

# Modulo matemáticas
import math

print(f"La raiz cuadrada de 10 es: {math.sqrt(10)}")
print(f"El numero pi es: {math.pi}")
print(f"Redondear al alza:  {math.ceil(6.56798)}")
print(f"Redondear a la baja: {math.floor(6.56798)}") #Redondea a la baja

# Modulo Random
import random

print(f"Numero aleatorio entre 15 y 67: {random.randint(15,70)}")#Aleatorio en ese intervalo.