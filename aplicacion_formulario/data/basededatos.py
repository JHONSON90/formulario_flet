import mysql.connector
import os

try:
    def connect_to_db():
        db = mysql.connector.connect(
            host="bhete2uv4pcbvdjlidml-mysql.services.clever-cloud.com",
            user="uh29qkzfhxeuyu2k",
            password=os.getenv('PASSWORD_CLEVER_CLOUD'),
            database="bhete2uv4pcbvdjlidml"
        )
        return db
except:
    print("Error de conexión a la base de datos")