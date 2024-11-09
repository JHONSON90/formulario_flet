import flet as ft
from views.dashboard import Dashboard

def main (page:ft.Page):
    page.title = "Formulario",
    
    page.add(Dashboard(page))
    
    page.vertical_alignment = "center",
    page.horizontal_alignment = "center",
    page.theme_mode = "light"    

ft.app(main, view=ft.AppView.WEB_BROWSER)