import flet as ft
from views_control import views_handler

def main(page: ft.Page):
    
    def route_change(route):
        print(page.route)
        page.views.clear()
        page.views.append(
            views_handler(page)[page.route]
        )
        
    page.on_route_change =  route_change
    page.go("/")

app(target=main)