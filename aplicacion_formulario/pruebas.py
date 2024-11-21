import flet as ft
import pickle
from views.formulario_cliente import Formulario_para_clientes
from views.registros_diarios import Formulario_Diario
from views.tabla_usuarios import Tabla_datos_clientes
from views.pagina_principal import Pagina_principal
from views.dashboard import Dashboard
from views.forgotpassword import ForgotPassword
from views.registro import Registro
from views.home import Login
import service.auth as auth_service
from views.navbar import navbar

class Main(ft.UserControl):
    def __init__(self, page: ft.Page,):
        super().__init__()
        self.page = page
        page.padding = 0
        page.bgcolor = ft.colors.INDIGO_50
        page.scroll = "auto"
        page.horizontal_alignment = "center",
        page.vertical_alignment = "center"
        page.theme_mode = "light"
        self.alignment = ft.alignment.center
        
        self.init()
        
        
        # self.theme_icon_button = ft.IconButton(
        #     ft.icons.DARK_MODE,
        #     selected=False,
        #     selected_icon=ft.icons.LIGHT_MODE,
        #     #icon_size=35,
        #     tooltip="Cambiar de tema",
        #     on_click=self.change_theme,
        #     style= ft.ButtonStyle(color={"":ft.colors.BLACK, "selected": ft.colors.WHITE})
        # )
        
    def init(self):
        self.page.on_route_change = self.on_route_change
        token = auth_service.load_token()
        
        if auth_service.authenticate_token(token):
            self.page.go('/home')            
        else:
            self.page.go('/login')        
        
    def on_route_change(self, e: ft.RouteChangeEvent): #1:13
        def view_pop(view):
            if len(self.page.views) > 1:
                self.page.views.pop()
                top_view = self.page.views[-1]
                self.page.go(top_view.route)
                
        view_pop(self.page.views[-1])
        
        public_routes = ["/login", "/signup", "/forgotpassword"]
        protected_routes = ["/home", "/dashboard", "/listado_clientes", "/registro_clientes", "/registros_diarios"]

        token = auth_service.load_token()
        is_autenticated = auth_service.authenticate_token(token)
        
        if e.route in protected_routes and not is_autenticated:
            print("acceso denegado: redirigiendo al login.")
            self.page.go('/login')
            return
        
             
        new_page = {
            "/login": Login,
            "/signup": Registro,
            "/forgotpassword": ForgotPassword,            
            "/home": Pagina_principal,            
            "/dashboard": Dashboard,
            "/listado_clientes":Tabla_datos_clientes,
            "/registro_clientes": Formulario_para_clientes,
            "/registros_diarios": Formulario_Diario
        }[e.route](self.page)
        
        self.page.views.clear()
        if e.route in public_routes:
            self.page.views.append(
                    ft.View(e.route,
                        [new_page],
                        bgcolor=ft.colors.INDIGO_50,
                        vertical_alignment="center",
                        horizontal_alignment="center"
                        )
                )
        else:
            self.page.views.append(
                ft.View(e.route,
                       [ ft.AppBar(
                            title=ft.Text(auth_service.get_name(token)),
                            bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST,
                            actions=[
                                ft.IconButton(ft.icons.HOME,
                                            tooltip= "Registro Nuevo Cliente",
                                                on_click=lambda _: self.page.go("/home")),
                                ft.IconButton(ft.icons.ASSIGNMENT_IND,
                                        tooltip= "Registro Nuevo Cliente",
                                            on_click=lambda _: self.page.go("/registro_clientes")),
                                
                                ft.IconButton(ft.icons.LIST_ROUNDED, 
                                            tooltip="Listado de Clientes",
                                            on_click = lambda _: self.page.go("/listado_clientes")),
                                ft.IconButton(ft.icons.ADD_CIRCLE, 
                                            tooltip="Crear Registro",
                                            on_click = lambda _: self.page.go("/registros_diarios")),
                                ft.IconButton(ft.icons.DASHBOARD,
                                            tooltip="Dashboard",
                                            on_click = lambda _: self.page.go("/dashboard")),
                                #self.theme_icon_button,
                                ft.PopupMenuButton(
                                    items=[
                                        ft.PopupMenuItem(
                                            text="Ajustes"
                                        ),
                                        ft.PopupMenuItem(
                                            text="Cerrar Sesion",
                                            on_click= lambda _: (auth_service.revoke_token(
                                                auth_service.load_token()), self.page.go('/login')),
                                        ),
                                        ]),
                            ]
                            
                        ),
                        new_page
                       ],
                       bgcolor=ft.colors.INDIGO_50,
                       vertical_alignment="center",
                       horizontal_alignment="center",
                    )
                )
        self.page.update()
            
    # def change_theme(e, self):
    #     self.page.theme_mode = "light" if self.page.theme_mode == "dark"  else "dark"
    #     self.theme_icon_button.selected = not self.theme_icon_button.selected
    #     self.page.update()
    
        
    

ft.app(target = Main, view=ft.AppView.WEB_BROWSER)

# def main(page: ft.Page):
#     page.title = "contador de prueba"
#     page.scroll = "auto"
#     page.alignment = "center"
#     page.theme_mode  = "LIGHT"
#     page.vertical_alignment= ft.MainAxisAlignment.CENTER # alineamos 
#     page.add(
#             Dashboard(page)
#         )

# ft.app(main)