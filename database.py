import sqlite3
import json

## CREACION Y CONEXION FACTURA EN LA BASE DE DATOS

DB_NAME = "facturas.db"

def obtener_conexion():
    return sqlite3.connect(DB_NAME) #Crea la conexion


def crear_base_datos():

    conexion = obtener_conexion()

    cursor = conexion.cursor() #Ejecuta la conexion

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS facturas(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    data TEXT

)
    """)
    conexion.commit()   

    conexion.close()

## GUARDAR FACTURA EN LA BASE DE DATOS

def guardar_factura(data):

    conexion = obtener_conexion()

    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO facturas(data)
        VALUES(?)
        """,
        (json.dumps(data),)
    )

    conexion.commit()

    conexion.close()

## OBTENER FACTURA DE LA BASE DE DATOS
def obtener_facturas():

    conexion = obtener_conexion()

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT data
        FROM facturas
    """)

    filas = cursor.fetchall()

    conexion.close()

    return filas    