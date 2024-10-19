import _mysql_connector as db
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

    def get_user(self, idClientes):
        query = "SELECT nombres FROM clientes WHERE idClientes = %s"
        self.cursor.execute(query,  (idClientes,))
        resultado =  self.cursor.fetchone()
        if resultado:
            return resultado[0]
        else:
            return None


    def delete_users(self,  idClientes):
        query = "DELETE FROM clientes WHERE idClientes = %s"
        self.cursor.execute(query)
        self.cursor.commit()
    
    def update_users(self, idClientes, nombres,telefono, correo ):
        query =  "UPDATE clientes SET nombres = %s, telefono = %s, correo = %s WHERE id =  %s"
        self.cursor.execute(query)
        self.cursor.commit()
        
    def add_registros(self, idClientes, valor, fecha, valor_servicio, tipo_de_servicio, usuario_final):
            tabla = "seguimiento"
            campos =  ["idClientes", "valor","fecha", "valor_servicio", "tipo_de_servicio", "usuario_final"]
            valores =  [idClientes, valor, fecha, valor_servicio, tipo_de_servicio, usuario_final]
            
            query = f"INSERT INTO {tabla} ({','.join(campos)}) VALUES (%s,%s,%s,%s,%s,%s)"
            self.cursor.execute(query, valores)
            self.mydb.commit()
            
        
    def get_registros(self):
        query = "SELECT * FROM seguimiento;"
        self.cursor.execute(query)
        registros = self.cursor.fetchall()
        return registros