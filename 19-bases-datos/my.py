import mysql.connector

#Conexion
database = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "",
  database = "master_python" 
)

#¿La conexion ha sido correcta?
#print(database)

cursor = database.cursor(buffered=True)#Es para que cuando ejecutamos muchas consultas con un cursor no nos falle

cursor.execute("CREATE DATABASE IF NOT EXISTS master_python") #Si no existe la base de datos la crea

"""
cursor.execute("SHOW DATABASES") #Almacena en el cursor una lista con todas las bases de datos que tienes

for bd in cursor:
  print(bd)
"""

# Crear tablas
cursor.execute("""
 CREATE TABLE IF NOT EXISTS vehiculos(
  id int(10) auto_increment not null,
  marca varchar(40) not null,
  modelo varchar(40) not null,
  precio float(10,2),
  CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")
"""
cursor.execute("SHOW TABLES")

for table in cursor:
  print(table)

cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18000)") #Inserta los datos fila a fila

coches = [
  ('SEAT', 'IBIZA', 5000),
  ('Citröen', 'C4', 3000),
  ('Ford', 'Mustang', 55000),
  ('Mercedes', 'Clase C', 35000)
]

cursor.executemany("INSERT INTO vehiculos VALUES(null, %s, %s, %s)", coches)

database.commit()
"""

cursor.execute("SELECT * FROM vehiculos WHERE precio <= 5000 AND marca = 'SEAT'")#Saca todos los datos de la base de datos
result = cursor.fetchall() #pasa los datos a una lista donde cada elemento es una fila de la base de datos
#esta fila a su vez es un vector donde cada posición equivale a una celda
#Listar
print("----TODOS LOS COCHES ----")
for coche in result:
  print(coche)

cursor.execute("SELECT * FROM vehiculos")
coche = cursor.fetchone()#Saca el primer elemento de la base de datos

#Borrar
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Mercedes'") #Borra los vehiculos de la marca Ford
database.commit()

print(cursor.rowcount, "borrados") #Devuelve el numero de registros que han sido borrados

# Actualizar
cursor.execute("UPDATE vehiculos SET modelo = 'León' WHERE marca = 'SEAT'")
database.commit()

print(cursor.rowcount, "Actualizados")