import flet as ft

def navbar():    
    return ft.Container(
        content= ft.AppBar(
            actions=[
                ft.IconButton(ft.icons.HOME,
                            tooltip= "Home",
                            on_click=lambda _: page.go("/home")),
                ft.IconButton(ft.icons.ASSIGNMENT_IND,
                            tooltip= "Registro Nuevo Cliente",
                            on_click=lambda _: page.go("/registro_clientes")),
                ft.IconButton(ft.icons.LIST_ROUNDED, 
                            tooltip="Listado de Clientes",
                            on_click = lambda _: page.go("/listado_clientes")),
                ft.IconButton(ft.icons.ADD_CIRCLE, 
                            tooltip="Crear Registro",
                            on_click = lambda _: page.go("/registros_diarios")),
                ft.IconButton(ft.icons.DASHBOARD,
                            tooltip="Dashboard",
                            on_click = lambda _: page.go("/dashboard")),
                ft.PopupMenuButton(
                            items=[
                                ft.PopupMenuItem(
                                    text="Ajustes"
                                    ),
                                ft.PopupMenuItem(
                                    text="Cerrar Sesion",
                                    #on_click= click_cerrar_sesion,
                                    )
                                ]
                            )
                        ]
                            
                    )
                )
    return navbarprueba
