import flet as ft 
from data.peticiones import UserManager

class Formulario_para_clientes(ft.UserControl):
    def __init__(self, page):
        super().__init__(expand=True)        
        self.page = page
        self.data = UserManager()
        
#region=: TEXT FIELDS DE LOS 4  CAMPOS

        self.idClientes = ft.TextField(value="",
                                 label="Identificacion",
                                 border_color="white",
                                 input_filter=ft.NumbersOnlyInputFilter(),
                                 )
        
        self.nombres = ft.TextField(value="",
                                 label="Nombres",
                                 border_color="white")
        
        self.telefono = ft.TextField(value="",
                                 label="Telefono",
                                 border_color="white",
                                 input_filter=ft.NumbersOnlyInputFilter()
                                 )
        
        self.correo = ft.TextField(value="",
                                 label="Correo",
                                 border_color="white")
        
        self.form = ft.Column(
            alignment= "center",
            horizontal_alignment= "center",
            controls=[
                ft.Container(
                    width=500,
                    border_radius=12,
                    padding= 40,
                    bgcolor="gray",
                    content= ft.Column(
                        horizontal_alignment="center",
                        controls=[
                            ft.Text(
                                "Registro de Clientes",
                                size=16,
                                color="white",
                                text_align="center"
                            ),
                    
                    self.idClientes,
                    self.nombres,
                    self.telefono,
                    self.correo,
                    ft.Container(
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.TextButton(
                                    text="Guardar",
                                    icon=ft.icons.SAVE,
                                    style=ft.ButtonStyle(
                                        color="white",
                                    ),
                                    on_click=self.add_data
                                ),
                                ft.TextButton(
                                    text="Listado de clientes",
                                    icon=ft.icons.LIST,
                                    style=ft.ButtonStyle(color="white"),
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
    
    def add_data(self, e):
        idClientes = self.idClientes.value
        nombres = self.nombres.value
        telefono = self.telefono.value
        correo = self.correo.value
        
        if idClientes != "" and nombres !=  "" and telefono != "" and correo != "":
            user_exist= False
            for row in self.data.get_users():
                if row[0] == idClientes:
                    user_exist = True
                    break
                if not user_exist:
                    self.clean_fields()
                    self.data.add_users(idClientes,nombres,telefono, correo),
                    self.show_data()
    
    def clean_fields(self):
        self.idClientes.value = ""
        self.nombres.value = ""
        self.telefono.value = ""
        self.correo.value = ""
        self.show_data()
           
    def build(self):
        return self.content