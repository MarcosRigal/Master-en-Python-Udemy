# Crear variables y asignarles un valor

texto = "Máster en Python"
texto2 = "con Víctor Robles"
numero = 45
decimal = 6.7

# Mostrar el valor de las variables

print(texto)
print(texto2)
print(numero)
print(decimal)

print("-----------------------")

# Sustituir el valor de algunas variables / reasignando valores

numero = 77
decimal = 8.9

print(numero)
print(decimal)

print("-----------------------")

# Concatenación

nombre = "Marcos"
apellidos = "Rivera Gavilán"
correo = "riveragavilanmarcos@gmail.com"

print(nombre + " " + apellidos + " - " + correo)
print(f"{nombre} {apellidos} - {correo}")
print("Hola me llamo {} {} y mi correo es {}".format(nombre, apellidos, correo))