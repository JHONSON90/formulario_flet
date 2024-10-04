import mysql.connector as db
from basededatos import connect_to_db

class UserManager():
    def  __init__(self):
        super().__init__()
    
        self.mydb = connect_to_db()        
        self.cursor = self.mydb.cursor()
        
    def add_users(self, idClientes, nombres, telefono, correo):
        tabla = "clientes"
        campos =  ["idClientes", "nombres", "telefono", "correo"]
        valores =  [idClientes, nombres, telefono, correo]
        
        query = f"INSERT INTO {tabla} ({','.join(campos)}) VALUES (%s,%s,%s,%s)"
        self.cursor.execute(query, valores)
        self.mydb.commit()
        
    def get_users(self):
        self.cursor.execute("SELECT * FROM  clientes")
        users = self.cursor.fetchall()
        return users

    def delete_users(self,  idClientes):
        query = "DELETE FROM clientes WHERE idClientes = %s"
        self.cursor.execute(query)
        self.cursor.commit()
    
    def update_users(self, idClientes, nombres,telefono, correo ):
        query =  "UPDATE clientes SET nombres = %s, telefono = %s, correo = %s WHERE id =  %s"
        self.cursor.execute(query)
        self.cursor.commit()
        


    
    # def close_mydb(self):
    #     self.mydb.close()

# x=UserManager()

# x.add_users(1,"Victor ", 123456, "victor@gmail.com")
# print(x.get_users())
