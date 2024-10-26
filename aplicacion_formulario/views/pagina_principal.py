import flet as ft 

class Pagina_principal(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        self.alignment = ft.alignment.center
        
        self.boton_registro_diario = ft.Container(
            content=ft.TextButton(
                "Registro Diario",
                on_click = lambda _: page.go("/registros_diarios")
            )
        )
        
        self.boton_crear_usuario = ft.Container(
            content=ft.TextButton(
                "Crear Usuario",
                on_click = lambda _: page.go("/registro_clientes")

            )
        )
        
        self.boton_Listado_usuarios = ft.Container(
            content=ft.TextButton(
                "Listar Usuarios",
                on_click = lambda _: page.go("/listado_clientes")

            )
        )
        
        self.boton_dashboar = ft.Container(
            content=ft.TextButton(
                "Dashboard",
                on_click = lambda _: page.go("/dashboard")
            )
        )
        
        
        self.listado_navegacion = ft.Container(
            border_radius=20,
            height=500,
            width=500,
            padding=20,
            content=ft.Column(
                alignment = ft.MainAxisAlignment.SPACE_EVENLY,
                controls=[
                    ft.Container(
                        ft.Text(
                            "Bienvenido  a la aplicacion /n Que vamos a realizar el dia de hoy?",
                            width=250,
                            weight="w900",
                            size=30,
                            text_align="center"
                        ),
                        padding= ft.padding.only(20,20)
                    ),
                    ft.Row(
                        alignment= ft.alignment.center,
                        controls=[
                            self.boton_registro_diario,
                            self.boton_crear_usuario,
                            self.boton_Listado_usuarios,
                            self.boton_dashboar
                        ]
                    )
                ]
            )
        )

        self.content = self.listado_navegacion
        
    def build(self):
        return self.content
        