import flet as ft

from pages.formulario import  Formulario
from pages.registros_diarios import Formulario_Diario
from pages.sidebar.py import  My_Sidebar

def views_handler(page):
    return {
        "/registro_diario":ft.View(
            route = "/registro_diario",
            controls=[
                Formulario_Diario(page)
            ]
        ),
        "/registro_clientes":ft.View(
            route = "registro_clientes",
            controls=[
                Formulario(page)
            ]
        ),
    }
    