print("Este programa imprime el intervalo entre los dos números introducidos")

inferior = int(input("Introduce el extremo inferior del intervalo: "))
superior = int(input("Introduce el extremo superior del intervalo: "))

if inferior > superior or inferior == superior:
  print("Error el intervalo no está bien definido.")
  breakpoint

for i in range((inferior + 1), superior):
  print(i)