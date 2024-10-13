import flet as ft

from formulario.pages.formulario_clientes import  Formulario
from formulario.pages.registros_diarios import Formulario_Diario
from formulario.pages.tabla_usuarios import  Tabla_datos_clientes


class Router():
    def  __init__(self, ft, page):
        self.page = page
        self.ft =  ft
        self.routes = {
                "/registros_diarios":ft.View(
                    route = "/registros_diarios",
                    controls=[
                        Formulario_Diario(page)
                    ]
                ),
                "/registro_clientes":ft.View(
                    route = "/registro_clientes",
                    controls=[
                        Formulario(page)
                    ]
                ),
                "/listado_clientes":ft.View(
                    route = "/listado_clientes",
                    controls=[
                        Tabla_datos_clientes(page)
                    ]
                ),
                "/dashboard":ft.View(
                    route = "/dashboard",
                    controls=[
                        Formulario_Diario(page)
                    ]
                ),
            }
        self.body = ft.container(self.routes["/"])
    
    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()
            