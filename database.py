import sqlite3
import json

## CREACION Y CONEXION FACTURA EN LA BASE DE DATOS

DB_NAME = "QComo.db"

def get_conexion():
    connection = sqlite3.connect(DB_NAME) #Crea la conexion

    connection.row_factory = sqlite3.Row # Agregando esta linea odas las consultas del proyecto empezarán a devolver objetos (tambien diccionarios) con nombres de columnas. y podremos acceder a las propiedades de user por medio de por ejemplo user["email"] y no en forma de tupla accediendo con el user[2] porque el [] con el tiempo olvidaremos el numero

    return connection


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

## CREAR USUARIO EN LA TABLA USERS
def create_user(name, email, password):

    conexion = get_conexion()

    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO users(name, email, password)
        VALUES (?, ?, ?)
        """,
        (name, email, password)
    )

    conexion.commit()

    conexion.close()        

def login_user(email, password):

    conexion = get_conexion()

    cursor = conexion.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE email = ?
        AND password = ?
        """,
        (email, password)
    )

    user = cursor.fetchone()

    conexion.close()

    return user

def get_user_by_email(email):

    conexion = get_conexion()

    cursor = conexion.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE email = ?
        """,
        (email,)
    )

    user = cursor.fetchone()

    conexion.close()

    return user