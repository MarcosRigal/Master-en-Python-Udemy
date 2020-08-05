print("Este programa calcula el tanto porciento del numero introducido")

numero = int(input("Introduce el numero al que deseas calcular el porcentaje: "))
porcentaje = (float(input("Que porcentaje deseas calcular: ")))/100

print(f"El {porcentaje*100}% de {numero} es: {porcentaje * numero}")