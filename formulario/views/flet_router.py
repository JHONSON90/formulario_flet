import flet as ft

from formulario.views.formulario_clientes import Formulario
from views.registros_diarios import Formulario_Diario
from views.tabla_usuarios import Tabla_datos_clientes


class Router:
    def __init__(self, page, ft):
        self.page = page
        self.ft = ft
        self.routes = {
            "/registros_diarios": Formulario_Diario(page),
            "/registro_clientes": Formulario(page),
            "/listado_clientes":  Tabla_datos_clientes(page),
            "/dashboard": Tabla_datos_clientes(page)

        }
        self.body = ft.Container(
            content = self.routes['/']
        )
    
    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()