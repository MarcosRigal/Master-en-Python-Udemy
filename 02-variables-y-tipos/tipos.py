nada = None
cadena = "Hola soy Marcos"
entero = 99
flotante = 4.2
booleano = True
lista = [10, 20, 30, 100, 200]
listaString = [44, "treinta",30, "cuarenta"]
tuplaNoCambia = ("master", "en", "python")
diccionario = {
    "nombre": "Marcos",
    "apellido": "Rivera Gavilán",
    "curso": "Master en Python"
}
rango = range(9)
dato_byte = b"Probando"

# Imprimir variable

print(nada)
print(cadena)
print(entero)
print(flotante)
print(booleano)
print(lista)
print(listaString)
print(tuplaNoCambia)
print(diccionario)
print(rango)
print(dato_byte)

# Mostrar tipo de dato

print(type(nada))
print(type(cadena))
print(type(entero))
print(type(flotante))
print(type(booleano))
print(type(lista))
print(type(listaString))
print(type(tuplaNoCambia))
print(type(diccionario))
print(type(rango))
print(type(dato_byte))

texto = "Hola soy un texto"
numerito = str(777)

print(f"{texto} {numerito}")

numerito = int(777)
print(type(numerito))

numerito = float(numerito)
print(type(numerito))