import flet as ft
from views.escoger_pqrs import Menu_expansible

def main(page : ft.Page):
    page.title = "PQRS"
    
    def change_theme(e):
        page.theme_mode =  "light" if page.theme_mode == "dark" else "dark"
        theme_icon_button.selected = not theme_icon_button.selected
        page.update()
        
    theme_icon_button = ft.IconButton(
        ft.icons.DARK_MODE,
        selected=False,
        selected_icon=ft.icons.LIGHT_MODE,
        tooltip="Cambiar de tema",
        on_click=change_theme,
        style= ft.ButtonStyle(color={"":ft.colors.BLACK, "selected": ft.colors.WHITE})
    )
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.Text("PQRS", size=50),
                    Menu_expansible(page)
                ]
            )
        )
        if page.route == "/formulario_pqrs":
            page.views.append(
                ft.View(
                    "/formulario_pqrs",
                    [
                        ft.Text("formulario pqrs", size=50)
                        #Listo para el formulario
                    ]
                )
            )
            page.update()
        
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.theme_mode = "light"
    page.on_view_pop = view_pop  
    page.go(page.route)

ft.app(main, view=ft.AppView.WEB_BROWSER)