import flet as ft
from pages.sidebar import My_Sidebar
from pages.formulario_clientes import Formulario_para_clientes
from pages.registros_diarios import Formulario_Diario
from pages.tabla_usuarios import Tabla_datos_clientes
from pages.home import Home

def  main(page: ft.Page):
    def route_change(route):
        page.views.clear()
        if page.route == "/registro_clientes":
            page.views.append(ft.View(
                "/registro_clientes",
                [sidebar,
                 ft.Container(
                     content=Formulario_para_clientes()
                 )
                 ]
            ))
        elif page.route == "/listado_clientes":
            page.views.append(ft.View(
                "/listado_clientes",
                [sidebar,
                 ft.Container(
                     content=Tabla_datos_clientes()
                 )
                 ]
            ))   
        elif page.route == "/registros_diarios":
            page.views.append(ft.View(
                "/registros_diarios",
                [sidebar,
                 ft.Container(
                     content=Formulario_Diario()
                 )
                 ]
            ))   
        elif page.route == "/dashboard":
            page.views.append(ft.View(
                "/dashboard",
                [sidebar,
                 ft.Container(
                     content=Tabla_datos_clientes()
                 )
                 ]
            ))   
        elif page.route == "/":
            page.views.append(ft.View(
                "/",
                [sidebar,
                 ft.Container(
                     content=Home()
                     )
                 ]
                ))
        page.update()
        
    sidebar = My_Sidebar(page)
    
    page.on_route_change = route_change
    
    page.go("/")

ft.app(target=main)