import flet as ft
from views.formulario_cliente import Formulario_para_clientes
from views.registros_diarios import Formulario_Diario
from views.tabla_usuarios import Tabla_datos_clientes

def main (page:ft.Page):
    page.title = "Formulario",
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(
                        title=ft.Text("Home"),
                        bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST,
                        actions=[
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
                                        text="Cerrar Sesion"
                                    )
                                    ]),
                        ]
                        
                    ),
                    ft.Text("Bienvenido a la aplicacion de registro de clientes"),
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
                                #Formulario_Diario(page)
                                ft.Text("colocar el formulario diario revisado y corregido aqui")
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
                                    ft.Text("Aqui va el dashBoard")
                                ]
                            )
                        )
            
        page.update()
        
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop  
    page.go(page.route)      

ft.app(main, view=ft.AppView.WEB_BROWSER)