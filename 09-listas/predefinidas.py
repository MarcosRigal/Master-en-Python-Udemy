cantantes = ["2Pac", "bbsita", "julio"]
numeros = [1, 9, 6, 4, 5]

# Ordenar
print(numeros)
numeros.sort()#Ejecuta el algoritmo de ordenación quickshort 
print(numeros)

# Añadir elementos

cantantes.append("Bisbal")#Append añade el elemento al final
cantantes.insert(2, "Chenoa")#Insert añade el elemento en la posición indicada

print(cantantes)

# Eliminar elementos
cantantes.pop(3)# Elimina el elemento con el indice introducido
cantantes.remove("bbsita")# Elimina el elemento que coincida con la cadena
print(cantantes)

# Dar la vuelta
print(numeros)
numeros.reverse() # Da la vuelta al string de numeros
print(numeros)

# Buscar dentro de una lista
print(9 in numeros) # Devuelve un booleano. True si la cadena se encuentra False si no se encuentra

# Contar elementos
print(len(numeros)) #Devuelve el numero de elementos de una lista

#Cuantas veces aparece un elemento
print(numeros.count(8))#Indica cuantas veces aparece un elemento en una lista

#Conseguir el indice
print(cantantes.index("2Pac")) #Devuelve el indice de la lista en la que se encuentra el elemento

#Unir listas
cantantes.extend(numeros)#Une dos listas una detras de la otra
print(cantantes)
