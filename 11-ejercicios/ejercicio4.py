def traducirTipo(tipo):
  result = None
  if tipo == list:
    result = "LISTA"
  elif tipo == str:
    result = "CADENA DE TEXTO"
  elif tipo == int:
    result = "NUMERO ENTERO"
  elif tipo == bool:
    result = "BOOLEANO"
  
  return result

def comprobarTipado(dato, tipo):
  test = isinstance(dato, tipo)
  if test:
    result = f"Este dato es del tipo {traducirTipo(tipo)}"
  else:
    result = "El tipo de dato no es correcto"
  return result

mi_lista = ["Hola mundo", 77]
titulo = "Master en Python"
numero = 12
verdadero = True

print(comprobarTipado(mi_lista, list))
print(comprobarTipado(titulo, list))
print(comprobarTipado(numero, list))
print(comprobarTipado(verdadero, bool))