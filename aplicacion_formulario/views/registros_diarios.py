import flet as ft
from datetime import datetime
from data.peticiones import UserManager

class Formulario_Diario(ft.UserControl):
    def __init__(self, page):
        super().__init__(expand=True)
        self.page = page
        page.bgcolor = ft.colors.INDIGO_50
        self.data = UserManager()
        self.alignment = ft.alignment.center        
        
        self.fecha_actual = datetime.now().strftime("%Y-%m-%d")
        
        self.idClientes = ft.Container(
            content=ft.TextField(
                border_color=ft.InputBorder.NONE,
                content_padding=ft.padding.only(
                    top=0, bottom=0, right=20, left=20
                ),
                hint_style= ft.TextStyle(
                    size=12,
                    color="#858796"
                ),
                hint_text="Identificacion",
                cursor_color="#858796",
                text_style= ft.TextStyle(
                    size=14,
                    color="black",
                ),
                input_filter=ft.NumbersOnlyInputFilter(),
                on_blur=self.busqueda_nombre
                
            ),
            border= ft.border.all(width=1, color="#bdcbf4"),
            border_radius = 20
        )
        
        self.nombres = ft.Container(
            content=ft.TextField(
                border_color=ft.InputBorder.NONE,
                content_padding=ft.padding.only(
                    top=0, bottom=0, right=20, left=20
                ),
                hint_style= ft.TextStyle(
                    size=12,
                    color="#858796"
                ),
                hint_text="Nombres y apellidos",
                cursor_color="#858796",
                text_style= ft.TextStyle(
                    size=14,
                    color="black",
                ),
                read_only=True
                
            ),
            border= ft.border.all(width=1, color="#bdcbf4"),
            border_radius = 20
        )
        
        self.usuario_final = ft.Container(
            content=ft.TextField(
                border_color=ft.InputBorder.NONE,
                content_padding=ft.padding.only(
                    top=0, bottom=0, right=20, left=20
                ),
                hint_style= ft.TextStyle(
                    size=12,
                    color="#858796"
                ),
                hint_text="Destinatario Transaccion",
                cursor_color="#858796",
                text_style= ft.TextStyle(
                    size=14,
                    color="black",
                ),
            ),
            border= ft.border.all(width=1, color="#bdcbf4"),
            border_radius = 20
        )
        
        self.tipo_de_servicio = ft.Container(
            content=ft.TextField(
                border_color=ft.InputBorder.NONE,
                content_padding=ft.padding.only(
                    top=0, bottom=0, right=20, left=20
                ),
                hint_style= ft.TextStyle(
                    size=12,
                    color="#858796"
                ),
                hint_text="Tipo de Servicio",
                cursor_color="#858796",
                text_style= ft.TextStyle(
                    size=14,
                    color="black",
                ),
            ),
            border= ft.border.all(width=1, color="#bdcbf4"),
            border_radius = 20
        )
        
        self.valor = ft.Container(
            content=ft.TextField(
                border_color=ft.InputBorder.NONE,
                content_padding=ft.padding.only(
                    top=0, bottom=0, right=20, left=20
                ),
                hint_style= ft.TextStyle(
                    size=12,
                    color="#858796"
                ),
                hint_text="Valor recibido en la transacción",
                cursor_color="#858796",
                text_style= ft.TextStyle(
                    size=14,
                    color="black",
                ),
                input_filter=ft.NumbersOnlyInputFilter(),              
            ),
            border= ft.border.all(width=1, color="#bdcbf4"),
            border_radius = 20
        )                 
        
        self.valor_del_servicio = ft.Container(
            content=ft.TextField(
                border_color=ft.InputBorder.NONE,
                content_padding=ft.padding.only(
                    top=0, bottom=0, right=20, left=20
                ),
                hint_style= ft.TextStyle(
                    size=12,
                    color="#858796"
                ),
                hint_text="Cuanto le cuesta al cliente la transacción",
                cursor_color="#858796",
                text_style= ft.TextStyle(
                    size=14,
                    color="black",
                ),
                input_filter=ft.NumbersOnlyInputFilter(),              
            ),
            border= ft.border.all(width=1, color="#bdcbf4"),
            border_radius = 20
        )
        
        self.form = ft.Column(
            alignment= "center",
            horizontal_alignment= "center",
            controls=[
                ft.Container(
                    width=500,
                    border_radius=12,
                    padding= 40,
                    bgcolor="white",
                    content= ft.Column(
                        horizontal_alignment="center",
                        controls=[
                            ft.Text(
                                "Registro de Transacciones",
                                size=16,
                                color="black",
                                text_align="center"
                            ),
                    
                    self.idClientes,
                    self.nombres,
                    self.tipo_de_servicio,
                    self.usuario_final,
                    self.valor,
                    self.valor_del_servicio,
                    ft.Container(height=0),
                    ft.Container(
                        alignment = ft.alignment.center,
                        bgcolor='#4e73df',
                        height=40,
                        border_radius=30,
                        content=ft.Text(
                            "Guardar Registro",
                        ),
                        on_click=self.add_data
                    ),
                    ft.Container(height=0),
                    ft.Container(
                        content=ft.Text(
                            "Ir a listado de usuarios",
                            color='#4e73df',
                            size=12
                        ),
                        on_click=lambda _: (
                                    self.page.go('/listado_clientes'))
                            ),
                    ft.Container(
                        content=ft.Text(
                            "Ir a Dashboart",
                            color='#4e73df',
                            size=12
                        ),
                        on_click=lambda _: (
                                    self.page.go('/dashboard'))
                            ),
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
        idClientes = self.idClientes.content.value 
        valor = self.valor.content.value
        fecha = self.fecha_actual
        valor_del_servicio = self.valor_del_servicio.content.value
        tipo_de_servicio = self.tipo_de_servicio.content.value
        usuario_final= self.usuario_final.content.value
        
        if len(idClientes) <=0 and  len(tipo_de_servicio) <=0 and len(usuario_final) <=0 and len(valor) <=0 and  len(valor_del_servicio) <=0:
            self.page.overlay.append(ft.SnackBar(ft.Text("Por favor complete todos los campos"), open=True))
            self.page.update()
        else:
            self.clean_fields()
            self.data.add_registros(idClientes, valor,  fecha, valor_del_servicio, tipo_de_servicio, usuario_final)
            self.page.overlay.append(ft.SnackBar(ft.Text("Registro agregado exitosamente"), open=True))
            
            
    def busqueda_nombre(self, e):
        id_Cliente =  self.idClientes.content.value
        nombre = self.data.get_user(id_Cliente)
                
        if nombre:
            self.nombres.content.value = nombre
        else:
            self.nombres.content.value = "Cliente no encontrado"
            self.page.overlay.append(ft.SnackBar(ft.Text("Cliente no encontrado favor agregar cliente"), open=True))
            self.page.update()
        
        self.update()
        
    def clean_fields(self):
        self.idClientes.content.value = ""
        self.nombres.content.value = ""
        self.tipo_de_servicio.content.value = ""
        self.usuario_final.content.value = ""
        self.valor.content.value = ""
        self.valor_del_servicio.content.value = ""
        self.update()
        
    def build(self):    
        return self.content