import flet as ft

class NavbarLayout(ft.UserControl):
    def __init__(self, content: ft.UserControl):
        super().__init__()
        self.content = content


    def build(self):
        return ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.AppBar(
                        title=ft.Text("Nombre Conjunto residencial"),
                        bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST,
                        actions=[
                            ft.TextButton("Home",                            on_click=lambda _: ft.Page.go("/home")),
                            ft.TextButton("Seguimiento",
                                        on_click=lambda _: ft.Page.go("/seguimiento")),
                            ft.PopupMenuButton(
                                items=[
                                    ft.PopupMenuItem(
                                        text="Ajustes"
                                        ),
                                    ft.PopupMenuItem(
                                        text="Cerrar Sesion",
                                        #on_click=click_cerrar_sesion
                                        )
                                    ]
                                ),
                            ]
                        ),
                self.content       
            ]
        )