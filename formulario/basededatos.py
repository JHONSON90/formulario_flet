import mysql.connector

try:
    def connect_to_db():
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1085917679JHon",
            database="formulario"
        )
        return db
except:
    print("Error de conexión a la base de datos")