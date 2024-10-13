import flet as ft

class My_Sidebar(ft.UserControl):
    def __init__(self,page):
        super().__init__(expand=True)
        
        self.page = page
        
        self.sidebar = ft.NavigationDrawer(
                    controls=[
                        ft.NavigationDrawerDestination(
                            icon=ft.Icon(ft.icons.ASSIGNMENT_IND),
                            # selected_icon=ft.Icon(ft.icons.ASSIGNMENT_IND_OUTLINED),
                            label="Crear Cliente",
                            on_click = lambda _: page.go("/registro_clientes")
                        ),
                        ft.NavigationDrawerDestination(
                            icon=ft.Icon(ft.icons.LIST_ROUNDED),
                            # selected_icon=ft.Icon(ft.icons.ASSIGNMENT_IND_OUTLINED),
                            label="Listado de Clientes",
                            on_click = lambda _: page.go("/listado_clientes")
                        ),
                        ft.NavigationDrawerDestination(
                            icon=ft.Icon(ft.icons.ADD_CIRCLE),
                            # selected_icon=ft.Icon(ft.icons.ADD_CIRCLE_OUTLINE_OUTLINED),
                            label="Crear Registro",
                            on_click = lambda _: page.go("/registros_diarios")
                        ),
                        ft.NavigationDrawerDestination(
                            icon=ft.Icon(ft.icons.DASHBOARD),
                            # selected_icon=ft.Icon(ft.icons.DASHBOARD_OUTLINED),
                            label="Dashboard",
                            on_click = lambda _: page.go("/dashboard")
                        ),
                    ],
                #     on_change=lambda e: print("selected destination: ", e.control.selected_index),
                #     ),
                #     ],
                # width=80,
                # height=700,
                # vertical_alignment=ft.CrossAxisAlignment.START
                ),
        
    def abrir_drawer(self, e):
        self.page.drawer = self.sidebar
        self.sidebar.open = True
        self.page.update()

    def build(self):
        return self.sidebar
            
