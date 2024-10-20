import flet as ft
from datetime import datetime
from data.peticiones import UserManager

class Formulario_Diario(ft.UserControl):
    def __init__(self, page):
        super().__init__(expand=True)
        self.page = page
        self.data = UserManager()
        self.alignment = ft.alignment.center        
        
        self.fecha_actual = datetime.now().strftime("%Y-%m-%d")
        
        self.idClientes = ft.TextField(
                value="",
                label="Identificacion",
                #border_color="white",
                input_filter=ft.NumbersOnlyInputFilter(),
                on_blur=self.busqueda_nombre
            )
   
        
        self.nombres = ft.TextField(
                value="",
                label="Nombres y Apellidos",
                read_only=True,
                border_color="white",              )
   
        
        self.usuario_final = ft.TextField(
                value="",
                label="Destinatario Transaccion",
                #border_color="white",
            )
           
        
        self.tipo_de_servicio = ft.TextField(
                value="",
                label="Tipo de servicio",
                #border_color="white",
            )
     
        
        self.valor = ft.TextField(
                value="",
                label="Valor Recibido",
                #border_color="white",
                input_filter=ft.NumbersOnlyInputFilter(),
            )
                 
        
        self.valor_del_servicio = ft.TextField(
                value="",
                label="Cuanto le cuesta al cliente la transaccion",
                #border_color="white",
                input_filter=ft.NumbersOnlyInputFilter(),
            )
        
        self.form = ft.Column(
            alignment= "center",
            horizontal_alignment= "center",
            controls=[
                ft.Container(
                    width=500,
                    border_radius=12,
                    padding= 40,
                    #bgcolor="gray",
                    content= ft.Column(
                        horizontal_alignment="center",
                        controls=[
                            ft.Text(
                                "Registro de Clientes",
                                size=16,
                                #color="white",
                                text_align="center"
                            ),
                    
                    self.idClientes,
                    self.nombres,
                    self.tipo_de_servicio,
                    self.usuario_final,
                    self.valor,
                    self.valor_del_servicio,
                    ft.Container(
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.TextButton(
                                    text="Guardar",
                                    icon=ft.icons.SAVE,
                                    # style=ft.ButtonStyle(
                                    #     color="white",
                                    # ),
                                    on_click=self.add_data
                                ),
                                ft.TextButton(
                                    text="Listado de clientes",
                                    icon=ft.icons.LIST,
                                    #style=ft.ButtonStyle(color="white"),
                                    on_click=lambda _: self.page.go("/listado_clientes")
                                                                    
                                )
                            ]
                        )
                    )
                ]
            )
        )
            ]
        ) 
        
        self.content = self.form
        
    #     self.formulario_vacio = ft.AlertDialog(
    #         modal=True,
    #         title="Error",
    #         content="El formulario esta  vacio",
    #         actions=ft.TextButton("Ok", on_click=self.close_dlg),
    #         actions_alignment=ft.MainAxisAlignment.END,
    #     )
        
    # def close_dlg(self, e):
    #     self.formulario_vacio.open =  False,
    #     e.contol.page.update()

    
    def add_data(self, e):
        idClientes = self.idClientes.value 
        valor = self.valor.value
        fecha = self.fecha_actual
        valor_del_servicio = self.valor_del_servicio.value
        tipo_de_servicio = self.tipo_de_servicio.value
        usuario_final= self.usuario_final.value
        
        if len(idClientes) <=0 and  len(tipo_de_servicio) <=0 and len(usuario_final) <=0 and len(valor) <=0 and  len(valor_del_servicio) <=0:
            print("formulario vacio")
        else:
            self.clean_fields()
            self.data.add_registros(idClientes, valor,  fecha, valor_del_servicio, tipo_de_servicio, usuario_final),
            
            
    def busqueda_nombre(self, e):
        id_Cliente =  self.idClientes.value
        nombre = self.data.get_user(id_Cliente)
                
        if nombre:
            self.nombres.value = nombre
        else:
            self.nombres.value = "Cliente no encontrado"
        
        self.update()
        
    def clean_fields(self):
        self.idClientes.value = ""
        self.nombres.value = ""
        self.tipo_de_servicio.value = ""
        self.usuario_final.value = ""
        self.valor.value = ""
        self.valor_del_servicio.value = ""
        self.update()
        
    def build(self):    
        return self.content