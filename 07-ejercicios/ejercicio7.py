print("Este programa imprime todos los numeros impares en el intervalo introducido por el usuario")

inferior = int(input("Introduce el extremo inferior del intervalo: "))
superior = int(input("Introduce el extremo superior del intervalo: "))

if inferior > superior or inferior == superior:
  print("Error el intervalo no ha sido bien definido.")
  breakpoint

for i in range((inferior+1), superior):
  if i % 2 != 0:
    print(i)