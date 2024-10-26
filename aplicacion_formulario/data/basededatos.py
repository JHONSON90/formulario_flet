import mysql.connector
import os

try:
    def connect_to_db():
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv('PASSWORD_MYSQL'),
            database="formulario"
        )
        return db
except:
    print("Error de conexión a la base de datos")