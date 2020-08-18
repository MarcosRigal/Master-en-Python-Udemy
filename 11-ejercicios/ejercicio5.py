tabla = [
  {
    "Categoría": "ACCIÓN",
    "Juegos": ["GTA", "COD", "PUGB"] 
  },
  {
    "Categoría": "AVENTURA",
    "Juegos": ["ASSASINS", "CRASH", "PRINCE"] 
  },
  {
    "Categoría": "DEPORTES",
    "Juegos": ["FIFA", "PRO", "MOTO GP"] 
  }  
]

for categoria in tabla:
 print(f"------------{categoria['Categoría']}------------")
 for juego in categoria['Juegos']:
   print(juego)
