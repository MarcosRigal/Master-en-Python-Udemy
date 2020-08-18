def imprime(numeros):
  for numero in numeros:
    print(numero)
  print("----------------------------")
numeros = [1,4,6,7,3,2,9,8]

imprime(numeros)

numeros.sort()

imprime(numeros)

print(f"Hay: {len(numeros)} numeros")

elemento = int(input("Introduce el elemento que desee buscar: "))

print(f"El elemento se encuetra en la posición: {numeros.index(elemento)+1}")