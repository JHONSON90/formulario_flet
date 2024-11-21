import flet as ft 
from views.navbar import navbar
from service.auth import get_name, load_token, revoke_token

class Pagina_principal(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        page.bgcolor = ft.colors.INDIGO_50
        page.horizontal_alignment = ft.MainAxisAlignment.CENTER,
        page.vertical_alignment = ft.CrossAxisAlignment.CENTER,
        self.alignment = ft.alignment.center
        
        self.current_user_name = get_name(load_token())
        
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
        
        self.theme_icon_button = ft.IconButton(
            ft.icons.DARK_MODE,
            selected=False,
            selected_icon=ft.icons.LIGHT_MODE,
            #icon_size=35,
            tooltip="Cambiar de tema",
            on_click=self.change_theme,
            style= ft.ButtonStyle(color={"":ft.colors.BLACK, "selected": ft.colors.WHITE})
    )      
        self.listado_navegacion = ft.Container(
            border_radius=20,
            height=500,
            width=500,
            padding=20,
            content= ft.Column(
                alignment = ft.MainAxisAlignment.SPACE_EVENLY,
                controls=[
                    ft.Container(
                        ft.Text(
                            f"Bienvenido  {self.current_user_name} Que vamos a realizar el dia de hoy?",
                            # width=900,
                            # weight=900,
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

    def change_theme(e, self):
        self.page.theme_mode = "light" if self.page.theme_mode == "dark"  else "dark"
        self.theme_icon_button.selected = not self.theme_icon_button.selected
        self.page.update()
        
    
    def build(self):
        return self.content
        