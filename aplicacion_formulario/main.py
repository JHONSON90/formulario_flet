import flet as ft
from views.formulario_cliente import Formulario_para_clientes
from views.registros_diarios import Formulario_Diario
from views.tabla_usuarios import Tabla_datos_clientes
from views.home import Login


def main (page:ft.Page):
    page.title = "Formulario",
    
    def change_theme(e):
        page.theme_mode = "light" if page.theme_mode == "dark"  else "dark"
        theme_icon_button.selected = not theme_icon_button.selected
        page.update()
        
    theme_icon_button = ft.IconButton(
        ft.icons.DARK_MODE,
        selected=False,
        selected_icon=ft.icons.LIGHT_MODE,
        #icon_size=35,
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
                   Login(page)
                   
                ]
            )
        )
        
        if page.route ==  "/registro_clientes":
            page.views.append(
                
                ft.View(
                    "/registro_clientes",
                    [
                        ft.AppBar(
                        title=ft.Text("Registro de Clientes"),
                        bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST,
                        actions=[
                            ft.IconButton(ft.icons.HOME,
                                          tooltip= "Registro Nuevo Cliente",
                                            on_click=lambda _: page.go("/")),
                            ft.IconButton(ft.icons.LIST_ROUNDED, 
                                          tooltip="Listado de Clientes",
                                          on_click = lambda _: page.go("/listado_clientes")),
                            ft.IconButton(ft.icons.ADD_CIRCLE, 
                                          tooltip="Crear Registro",
                                          on_click = lambda _: page.go("/registros_diarios")),
                            ft.IconButton(ft.icons.DASHBOARD,
                                          tooltip="Dashboard",
                                          on_click = lambda _: page.go("/dashboard")),
                            theme_icon_button,
                            ft.PopupMenuButton(
                                items=[
                                    ft.PopupMenuItem(
                                        text="Ajustes"
                                    ),
                                    ft.PopupMenuItem(
                                        text="Cerrar Sesion"
                                    )
                                    ]),
                        ]
                        
                    ),
                        Formulario_para_clientes(page)
                    ]
                )
            )
            
        if page.route ==  "/listado_clientes":
            page.views.append(
                ft.View(
                    "/listado_clientes",
                    [
                    ft.AppBar(
                        title=ft.Text("Listado de Clientes"),
                        bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST,
                        actions=[
                            ft.IconButton(ft.icons.HOME,
                                        tooltip= "Home",
                                            on_click=lambda _: page.go("/")),
                            ft.IconButton(ft.icons.ASSIGNMENT_IND,
                                      tooltip= "Registro Nuevo Cliente",
                                        on_click=lambda _: page.go("/registro_clientes")),
                            ft.IconButton(ft.icons.ADD_CIRCLE, 
                                        tooltip="Crear Registro",
                                        on_click = lambda _: page.go("/registros_diarios")),
                            ft.IconButton(ft.icons.DASHBOARD,
                                        tooltip="Dashboard", 
                                        on_click = lambda _: page.go("/dashboard")),
                            theme_icon_button,
                            ft.PopupMenuButton(
                                items=[
                                    ft.PopupMenuItem(
                                        text="Ajustes"
                                    ),
                                    ft.PopupMenuItem(
                                        text="Cerrar Sesion"
                                    )
                                    ]),
                        ]
                        
                    ),
                        Tabla_datos_clientes(page)
                    ]
                )
            )
                
        if page.route ==  "/registros_diarios":
                page.views.append(
                    ft.View(
                        "/registros_diarios",
                        [
                            ft.AppBar(
                            title=ft.Text("Registro Transacción"),
                            bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST,
                            actions=[
                                ft.IconButton(ft.icons.HOME,
                                             tooltip= "Home",
                                             on_click=lambda _: page.go("/")),
                                ft.IconButton(ft.icons.ASSIGNMENT_IND,
                                            tooltip= "Registro Nuevo Cliente",
                                            on_click=lambda _: page.go("/registro_clientes")),
                                ft.IconButton(ft.icons.LIST_ROUNDED, 
                                             tooltip="Listado de Clientes",
                                             on_click = lambda _: page.go("/listado_clientes")), 
                                ft.IconButton(ft.icons.DASHBOARD,
                                              tooltip="Dashboard",
                                              on_click = lambda _: page.go("/dashboard")),
                                theme_icon_button,
                                ft.PopupMenuButton(
                                        items=[
                                            ft.PopupMenuItem(
                                                text="Ajustes"
                                            ),
                                            ft.PopupMenuItem(
                                                text="Cerrar Sesion"
                                            )
                                            ]),
                                ]
                                
                            ),
                                
                                Formulario_Diario(page),
                                  ]
                        )
                    )
                    
        if page.route ==  "/dashboard":
            page.views.append(
                ft.View(
                    "/dashboard",
                                [
                                    ft.AppBar(
                                    title=ft.Text("DashBoard"),
                                    bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST,
                                    actions=[
                                        ft.IconButton(ft.icons.HOME,
                                                    tooltip= "Home",
                                                        on_click=lambda _: page.go("/")),
                                        ft.IconButton(ft.icons.ASSIGNMENT_IND,
                                                tooltip= "Registro Nuevo Cliente",
                                                    on_click=lambda _: page.go("/registro_clientes")),
                                        ft.IconButton(ft.icons.LIST_ROUNDED, 
                                                    tooltip="Listado de Clientes",
                                                    on_click = lambda _: page.go("/listado_clientes")),
                                        ft.IconButton(ft.icons.ADD_CIRCLE, 
                                                    tooltip="Crear Registro",
                                                    on_click = lambda _: page.go("/registros_diarios")),
                                        theme_icon_button,
                                        ft.PopupMenuButton(
                                            items=[
                                                ft.PopupMenuItem(
                                                    text="Ajustes"
                                                ),
                                                ft.PopupMenuItem(
                                                    text="Cerrar Sesion"
                                                )
                                                ]),
                                    ]
                                    
                                ),
                                    ft.Text("Aqui va el dashBoard"),
                                ]
                            )
                        )
            
        page.update()
        
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.vertical_alignment = "center",
    page.horizontal_alignment = "center",
    page.theme_mode = "light"
    page.on_view_pop = view_pop  
    page.go(page.route)      

ft.app(main, view=ft.AppView.WEB_BROWSER)