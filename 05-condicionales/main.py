"""
 Operadores de comparación:
 == igual
 != diferente
 < menor que
 > mayor que 
 <= menor o igual que
 >= mayor o igual que

 Operadores lócos:
 and Y
 or O
 ! Negación 
 not NO
"""

# Ejemplo 1
print("######## Ejemplo 1 ###########")

color = input("Adivina cual es mi color favorito: ")

if color == "rojo":
    print("Enhorabuena!!")
    print("El color es Rojo")

else:
    print("Color incorrecto!!")

# Ejemplo 2
print("####### Ejemplo 2 #######")

year = int(input("¿En que año estamos?"))

if year >= 2021:
    print("Estamos de 2021 en adelante")
else:
    print("Es un año anterion a 2021")

# Ejemplo 3
print("###### Ejemplo 3 #######")

nombre = "Marcos"
ciudad = "Córdoba"
continente = "Europa"
edad = 19
mayoria_edad = 18

if edad > mayoria_edad:
    print(f"{nombre} es mayor de edad")
    if continente == "Europa":
        print(f"Es europeo y de {ciudad}")

    else:
        print("No es europeo")
else:
    print(f"{nombre} no es mayor de edad")

# Ejemplo 4
print("###### Ejemplo 4 #######")

dia = int(input("Introduce un numero para saber el día de la semana: "))

if dia == 1:
    print("Es lunes")

elif dia == 2:
    print("Es martes")

elif dia == 3:
    print("Es miercoles")

elif dia == 4:
    print("Es jueves")

elif dia == 5:
    print("Es viernes")

else:
    print("Es fin de semana")


# Ejemplo 5
print("###### Ejemplo 5 #######")

edad_minima = 18
edad_maxima = 65
edad_real = int(input("Introduce tu edad: "))

if edad_real < edad_minima or edad_real > edad_maxima:
    print("No esta en edad de trabajar")

else:
    print("Esta en edad de trabajar")


# Ejemplo 6
print("###### Ejemplo 6 #######")

pais = "España"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print("Es un pais de habla hispana")

else:
    print("No es un pais de habla hispana")

# Ejemplo 7
print("###### Ejemplo 7 #######")

pais = "Inglaterra"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print("No es un pais de habla hispana")

else:
    print("Es un pais de habla hispana")

# Ejemplo 8
print("###### Ejemplo 8 #######")

pais = "España"

if pais != "Mexico" and pais == "España" and pais == "Colombia":
    print("No es un pais de habla hispana")

else:
    print("Es un pais de habla hispana")