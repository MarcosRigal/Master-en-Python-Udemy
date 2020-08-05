aprobados = 0 
suspensos = 0

for i in range(15):
  nota = float(input("Introduce la nota del alumno: "))
  while nota > 10 or nota < 0:
    nota = float(input("Error introduce una nota válida: "))
  if nota >= 5.00:
    aprobados += 1
  else:
    suspensos += 1

print(f"Han aprobado: {aprobados}, y han suspendido: {suspensos}")