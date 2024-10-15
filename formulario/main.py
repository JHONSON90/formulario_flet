import flet as ft
from pages.sidebar import my_Sidebar
from pages.formulario_clientes import Formulario_para_clientes
from pages.registros_diarios import Formulario_Diario
from pages.tabla_usuarios import Tabla_datos_clientes
from pages.home import Home

def  main(page: ft.Page):
    rutas = {
    "/registro_clientes": Formulario_para_clientes(page),
    "/listado_clientes": Tabla_datos_clientes(page),
    "/registros_diarios": Formulario_Diario(page),
    "/dashboard": Tabla_datos_clientes(page),
    "/": ft.Text("Welcome my page", color=ft.colors.CYAN_100)
}
    
    def route_change(route):
        page.views.clear()
        if page.route in rutas:
            print(f"Ruta activa: {page.route}")
             
        if page.route in rutas:
            print(f"Ruta activa: {page.route}")
            print(f"Componente cargado: {rutas[page.route]}")
            page.views.append(ft.View(
                page.route, 
                [
                    ft.Row(
                        controls=[
                            sidebar2,
                            rutas[page.route]
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment= ft.CrossAxisAlignment.START
                    )
                ]
            )
            )
            page.update()
        
    sidebar2 = my_Sidebar(page)
    page.on_route_change = route_change
    #page.auto_scroll = True,
    #page.scroll = "auto",
    #page.dark_theme = True,
    page.go("/")
    

ft.app(target=main)