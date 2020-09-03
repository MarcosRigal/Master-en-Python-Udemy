# Importar el modulo

import sqlite3

# Conexion
conexion = sqlite3.connect("./19-bases-datos/pruebas.db")

# Crear cursor
cursor = conexion.cursor()

# Crear una tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
id INTEGER PRIMARY KEY AUTOINCREMENT,
titulo varchar(255),
descripcion text, 
precio int(255)
);
""")

# Insertar datos
cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto', 'Descripcion de mi producto', 550)")

# Borrar registros
#cursor.execute("DELETE FROM productos")

# Insertar muchos registros de golpe
productos = [
  ("Portatil", "Buen PC", 700),
  ("Movil", "Buen Movil", 800),
  ("Placa base", "Buena placa", 80),
  ("Tablet 10", "Buena tablet", 300),
]
cursor.executemany("INSERT INTO productos VALUES (null, ?, ?, ?)", productos)

# Actualizar datos 
cursor.execute("UPDATE productos SET precio = 600 WHERE precio = 80")

# Guardar cambios
conexion.commit()

# Listar datos
cursor.execute("SELECT * FROM productos;") #Si quieres filtrar es: "SELECT * FROM productos WHERE precio < 100"
productos = cursor.fetchall()
print(productos)

# Sacar el primer elemento
producto = cursor.fetchone()

# Cerrar la conexion
conexion.close()