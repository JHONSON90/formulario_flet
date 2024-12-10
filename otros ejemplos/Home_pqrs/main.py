import flet as ft 
from components.compo_home import MenuHome

def main(page: ft.Page):
    page.title = "contador de prueba"
    page.scroll = "auto"
    page.alignment = "center"
    page.theme_mode  = "LIGHT"
    page.vertical_alignment= ft.MainAxisAlignment.CENTER # alineamos 
    page.add(
            MenuHome()
        )

ft.app(main)