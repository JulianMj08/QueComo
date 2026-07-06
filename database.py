import sqlite3

conexion = sqlite3.connect("facturas.db") #Crea la conexion

cursor = conexion.cursor() #Ejecuta la conexion

def crear_base_datos():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS facturas(

id INTEGER PRIMARY KEY AUTOINCREMENT,

data TEXT

)
    """)
    conexion.commit()   