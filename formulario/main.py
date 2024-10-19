import flet as ft
#from views.sidebar import my_Sidebar
from views.formulario_clientes import Formulario_para_clientes
from views.registros_diarios import Formulario_Diario
from views.tabla_usuarios import Tabla_datos_clientes
from views.home import Home
from flet import AppBar, ElevatedButton, Page, Text, View, colors

def  main(page: ft.Page):
#   rutas = {
#     "/": Home,
#     "/registro_clientes": Formulario_para_clientes,
#     "/listado_clientes": Tabla_datos_clientes,
#     "/registros_diarios": Formulario_Diario,
#     "/dashboard": Tabla_datos_clientes,
# }
    
    def route_change(route):
        page.views.clear()
        page.views.append(
                View("/", 
                        [   
                            AppBar(title = Text("Home"), bgcolor = colors.WHITE30 ),
                            Home(page)
                        ]
                        )
                )
        if page.route == "/registro_clientes":
            page.views.append(
                View(
                        "/registro_clientes",
                        [   
                            AppBar(title = Text("Formulario Clientes"), bgcolor = colors.WHITE30 ),
                            Formulario_para_clientes(page)
                            ]
                        )
                    )
        elif page.route == "/listado_clientes":
            page.views.append(
                View(
                   [
                        AppBar(title = Text("Tabla de datos"), bgcolor = colors.WHITE30 ),
                       Tabla_datos_clientes(page)
                       ]
                    )
                  )
        elif page.route == "/registros_diarios":
                page.views.append(
                    View(
                        "/registros_diarios",
                        [
                            AppBar(title = Text("Formulario diario"), bgcolor = colors.WHITE30 ),
                             Formulario_Diario(page)
                             ]
                        )
                    )
        elif page.route == "/dashboard":
                page.views.append(
                    View(
                        "/dashboard",
                        [
                             AppBar(title = Text("dashboard"), bgcolor = colors.WHITE30 ),
                             Tabla_datos_clientes(page)
                             ]
                        )
                    )
        page.update()
        
    
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    #page.auto_scroll = True,
    #page.scroll = "auto",
    #page.dark_theme = True,
    page.go(page.route)
    

ft.app(main)