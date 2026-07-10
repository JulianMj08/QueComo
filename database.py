import sqlite3
import json

## CREACION Y CONEXION FACTURA EN LA BASE DE DATOS

DB_NAME = "QComo.db"

def get_conexion():
    return sqlite3.connect(DB_NAME) #Crea la conexion


def create_db():

    conexion = get_conexion()

    cursor = conexion.cursor() #Ejecuta la conexion

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    data TEXT

)
    """)
    conexion.commit()   

    conexion.close()

## GUARDAR FACTURA EN LA BASE DE DATOS

def save_ticket(data):

    conexion = get_conexion()

    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO tickets(data)
        VALUES(?)
        """,
        (json.dumps(data),)
    )

    conexion.commit()

    conexion.close()

## OBTENER FACTURA DE LA BASE DE DATOS
def get_ticket():

    conexion = get_conexion()

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT data
        FROM tickets
    """)

    rows = cursor.fetchall()

    conexion.close()

    return rows    