# Programación orientada a objetos (POO o OOP)

# Definir una clase (Es un molde para crear mas objetos de ese tipo con caracteristicas similares)

class Coche:
  
  # Atributos o propiedades (son publicas) (variables)
  # Características del coche:
  color = "Rojo"
  marca = "Ferrari"
  modelo = "Aventador"
  velocidad = 300
  caballaje = 500
  plazas = 2
  # Métodos, son acciones que hace el objeto (coche)(Son funciones)
  def setColor(self, color):
    self.color = color
  
  def getColor(self):
    return self.color
  
  def setModelo(self, modelo):
    self.modelo = modelo

  def getModelo(self):
    return self.modelo

  def acelerar(self):
    self.velocidad += 1
  
  def frenar(self):
    self.velocidad -=1
  
  def getVelocidad(self):
    return self.velocidad
# Fin definición clase

# Crear objetos / Instanciar clase
print("Coche 1")
coche = Coche()
coche.setColor("Marron")
coche.setModelo("Murcielago")

print(coche.marca, coche.getModelo(), coche.getColor())
print("Velocidad actual: ", coche.getVelocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()

print("Velocidad actual: ", coche.getVelocidad())

print("-----------------------------")
# Crear mas objetos
print("Coche 2")
coche2 = Coche()
coche2.setColor("Verde")
coche2.setModelo("Gallardo")

print(coche2.getColor())
print(coche2.marca, coche2.getModelo(), coche2.getColor())

print(type(coche2))