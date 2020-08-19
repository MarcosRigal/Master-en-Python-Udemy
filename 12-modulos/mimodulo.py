
def holaMundo(nombre):
  return f"Hola que tal estas, {nombre}"

def calculadora(n1, n2, basicas = False):
  
  suma = n1 + n2
  resta = n1 - n2
  multi = n1 * n2
  div = n1 / n2

  cadena = ""
  if basicas != False:
    cadena += "Suma:" + str(suma)
    cadena += "Resta: " + str(resta)

  else:
    cadena += "Producto: " + str(multi)
    cadena += "Division: " + str(div)
  
  return cadena