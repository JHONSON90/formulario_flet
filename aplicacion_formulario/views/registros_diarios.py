import flet as ft
from datetime import datetime
from data.peticiones import UserManager

class Formulario_Diario(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        page.padding = 0
        self.data = UserManager()
        self.expand=True
        self.alignment = ft.alignment.center
        self.error_border = ft.border.all(width=1,color="red")
        
        self.fecha_actual = datetime.now().strftime("%Y-%m-%d")
        
        self.idClientes = ft.TextField(
                value="",
                label="Identificacion",
                border_color="white",
                input_filter=ft.NumbersOnlyInputFilter(),
                on_blur=self.busqueda_nombre
            ),
   
        
        self.nombres = ft.TextField(
                value="",
                label="Nombres y Apellidos",
                read_only=True,
                border_color="white",
            ),
   
        
        self.usuario_final = ft.TextField(
                value="",
                label="Destinatario Transaccion",
                border_color="white",
            ),
           
        
        self.tipo_de_servicio = ft.TextField(
                value="",
                label="Tipo de servicio",
                border_color="white",
            ),
     
        
        self.valor = ft.TextField(
                value="",
                label="Valor Recibido",
                border_color="white",
                input_filter=ft.NumbersOnlyInputFilter(),
            ),
                 
        
        self.valor_del_servicio = ft.TextField(
                value="",
                label="Cuanto le cuesta al cliente la transaccion",
                border_color="white",
                input_filter=ft.NumbersOnlyInputFilter(),
            ),
        
        self.form_registro_clientes = ft.Column(
                            horizontal_alignment="center",
                            controls=[
                                ft.Text(
                                    "Registro de Transacciones",
                                    size=16,
                                    text_align="center"
                                ),                            
                                self.idClientes,
                                self.nombres,
                                self.tipo_de_servicio,
                                self.usuario_final,
                                self.valor,
                                self.valor_del_servicio,
                                ft.Row(
                                        alignment= ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.TextButton(
                                                "Guardar",
                                                icon=ft.icons.SAVE,
                                        on_click= self.add_data
                                        ),
                                            ],
                                        ),
                            ],
                            
                                    )
        self.content = self.form_registro_clientes
        
        self.formulario_vacio = ft.AlertDialog(
            modal=True,
            title="Error",
            content="El formulario esta  vacio",
            actions=ft.TextButton("Ok", on_click=self.close_dlg),
            actions_alignment=ft.MainAxisAlignment.END,
        )
        
    def close_dlg(self, e):
        self.formulario_vacio.open =  False,
        e.contol.page.update()

    
    
    
    def clean_fields(self):
        self.idClientes.value = ""
        self.nombres.value = ""
        self.tipo_de_servicio.value = ""
        self.usuario_final.value = ""
        self.valor.value = ""
        self.valor_del_servicio.value = ""
        
    
    
    
    def add_data(self, e):
        idClientes = self.idClientes.value 
        valor = self.valor.value
        fecha = self.fecha_actual.value
        valor_del_servicio = self.valor_del_servicio.value
        tipo_de_servicio = self.tipo_de_servicio.value
        usuario_final= self.usuario_final.value
        
        if idClientes == "" and  tipo_de_servicio == "" and usuario_final == "" and valor == "" and  valor_del_servicio == "":
            print("formulario vacio")
        else:
            self.clean_fields()
            self.data.add_registros(idClientes, valor,  fecha, valor_del_servicio, tipo_de_servicio, usuario_final),
            self.update()
            
    def busqueda_nombre(self, e):
        id_Cliente =  self.idClientes.value
        nombre = self.data.get_user(id_Cliente)
                
        if nombre:
            self.nombres.value = nombre
        else:
            self.nombres.value = "Cliente no encontrado"
        
        self.update()
        
    def build(self):
        return self.content