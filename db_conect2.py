import mysql.connector as db

class UserManager():
    def __init__(self):
        super().__init__()
        # Establecer conexión con la base de datos
        self.mydb = db.connect(
            user='root',
            password='iDea.2022*',
            host='localhost',
            database='p38zvljh_iclinic2'
        )
        # Crear el cursor
        self.cursor = self.mydb.cursor()

    def add_users(self, name, age):
        tabla = "usuarios_prueba"
        campos = ["name", "age"]
        valores = [name, age]

        query = f"INSERT INTO {tabla} ({', '.join(campos)}) VALUES (%s, %s)"
        self.cursor.execute(query, valores)
        self.mydb.commit()        

    def get_users(self):
        self.cursor.execute("SELECT * FROM usuarios_prueba")
        users = self.cursor.fetchall()
        return users

    def delete_users(self, name):
        query = "DELETE FROM usuarios_prueba WHERE name =?"
        self.cursor.execute("DELETE FROM usuarios_pruebas WHERE name =?")
        self.cursor.commit()        

    def update_users(self, id, name, age):
        query = '''UPDATE usuarios_prueba SET name = ?, age = ? WHERE id = ?'''
        self.cursor.execute('''UPDATE usuarios_pruebas SET name = ?, age = ? WHERE id = ?''')
        self.cursor.commit()        

    def close_mydb(self):
        self.mydb.close()

#x=UserManager()

#print(x.get_users())

