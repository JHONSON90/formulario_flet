import flet as ft 
from data.peticiones import UserManager

class Formulario_para_clientes(ft.UserControl):
    def __init__(self, page):
        super().__init__(expand=True)        
        self.page = page
        self.data = UserManager()
        self.alignment = ft.alignment.center
        
#region=: TEXT FIELDS DE LOS 4  CAMPOS

        self.idClientes = ft.Container(
            content= ft.TextField(
                border= ft.InputBorder.NONE,
                content_padding= ft.padding.only(
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
            ),
            border= ft.border.all(width=1, color="#bdcbf4"),
            border_radius = 20
        )
        
        
        
        self.nombres = ft.Container(
            content= ft.TextField(
                border= ft.InputBorder.NONE,
                content_padding= ft.padding.only(
                    top=0, bottom=0, right=20, left=20
                ),
                hint_style= ft.TextStyle(
                    size=12,
                    color="#858796"
                ),
                hint_text="Nombres",
                cursor_color="#858796",
                text_style= ft.TextStyle(
                    size=14,
                    color="black",
                ),
            ),
            border= ft.border.all(width=1, color="#bdcbf4"),
            border_radius = 20
        )
        
        self.telefono = ft.Container(
            content= ft.TextField(
                border= ft.InputBorder.NONE,
                content_padding= ft.padding.only(
                    top=0, bottom=0, right=20, left=20
                ),
                hint_style= ft.TextStyle(
                    size=12,
                    color="#858796"
                ),
                hint_text="Telefono",
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
        
        self.correo = ft.Container(
            content= ft.TextField(
                border= ft.InputBorder.NONE,
                content_padding= ft.padding.only(
                    top=0, bottom=0, right=20, left=20
                ),
                hint_style= ft.TextStyle(
                    size=12,
                    color="#858796"
                ),
                hint_text="Correo Electronico",
                cursor_color="#858796",
                text_style= ft.TextStyle(
                    size=14,
                    color="black",
                ),
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
                                "Registro de Clientes",
                                size=16,
                                color="black",
                                text_align="center"
                            ),
                    
                    self.idClientes,
                    self.nombres,
                    self.telefono,
                    self.correo,
                    ft.Container(height=0),
                    ft.Container(
                        alignment=ft.alignment.center,
                                bgcolor='#4e73df',
                                height=40,
                                border_radius=30,
                                content=ft.Text(
                                    "Guardar Cliente",
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
                        ]    
                                )
                )
                            ]
                        )
              
        self.content = self.form
    
    def add_data(self, e):
        idClientes = self.idClientes.content.value
        nombres = self.nombres.content.value
        telefono = self.telefono.content.value
        correo = self.correo.content.value
        
        if idClientes != "" and nombres !=  "" and telefono != "" and correo != "":
            user_exist = False
            
            for row in self.data.get_users():
                if row[0] == idClientes:
                    user_exist = True
            
            if user_exist:
                self.clean_fields()
                self.page.overlay.append(ft.SnackBar(ft.Text("El cliente ya existe"), open= True))
            else:
                self.clean_fields()
                success = self.data.add_users(idClientes, nombres, telefono, correo)
                if success:
                    self.page.overlay.append(ft.SnackBar(ft.Text("Cliente agregado exitosamente"), open=True))
                else:
                    self.page.overlay.append(ft.SnackBar(ft.Text("Error al agregar cliente"), open=True))
            self.page.update()
        else:
            self.page.overlay.append(ft.SnackBar(ft.Text("Por favor complete todos los campos"), open=True))
        self.page.update()
    
    def clean_fields(self):
        self.idClientes.content.value = ""
        self.nombres.content.value = ""
        self.telefono.content.value = ""
        self.correo.content.value = ""
        self.update()
    
           
    def build(self):
        return self.content