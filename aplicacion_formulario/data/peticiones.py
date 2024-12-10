import _mysql_connector as db
from data.basededatos import connect_to_db

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
        try:
            self.cursor.execute(query, valores)
            self.mydb.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
    
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

    def total_recibido(self):
        query = "SELECT SUM(valor) FROM seguimiento;"
        self.cursor.execute(query)
        registro = self.cursor.fetchone()
        return registro
    
    def total_cobrado(self):
        query = "SELECT SUM(valor_servicio) FROM seguimiento;" 
        
        # SELECT TOTAL_SS FROM total_servicios
        self.cursor.execute(query)
        registro = self.cursor.fetchone()
        return registro
        
    def total_recibido_mensual(self):
        query = "SELECT MONTH(fecha), SUM(valor) FROM seguimiento GROUP BY MONTH(fecha)"
        self.cursor.execute(query)
        registros = self.cursor.fetchall()
        return registros
    
    def total_cobrado_mensual(self):
        query = "SELECT MONTH(fecha), SUM(valor_servicio) FROM seguimiento GROUP BY MONTH(fecha)"
        self.cursor.execute(query)
        registros = self.cursor.fetchall()
        return registros
        
    def total_recibido_tipos(self):
        query = "SELECT tipo_de_servicio, SUM(valor) FROM seguimiento GROUP BY tipo_de_servicio"
        self.cursor.execute(query)
        registros = self.cursor.fetchall()
        return registros
    
    def minimo_recibido(self):
        query = "SELECT MIN(valor) FROM seguimiento;"
        self.cursor.execute(query)
        registro = self.cursor.fetchone()
        return registro
    
    def maximo_recibido(self):
        query = "SELECT MAX(valor) FROM seguimiento;"
        self.cursor.execute(query)
        registro = self.cursor.fetchone()
        return registro
        
    def minimo_cobrado(self):
        query = "SELECT MIN(valor_servicio) FROM seguimiento;"
        self.cursor.execute(query)
        registro = self.cursor.fetchone()
        return registro
    
    def maximo_cobrado(self):
        query = "SELECT MAX(valor_servicio) FROM seguimiento;"
        self.cursor.execute(query)
        registro = self.cursor.fetchone()
        return registro
