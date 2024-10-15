import flet as ft

def my_Sidebar(page: ft.page):
    sidebar =      ft.Container(
            width=80,
            height=740,
            border=ft.border.all(color="red"),
            content= ft.Column(
                controls=[
                            ft.IconButton(ft.icons.ASSIGNMENT_IND, 
                                            tooltip= "Registro Nuevo Cliente",
                                            on_click=lambda _: page.go("/registro_clientes")),
                            #selected_icon=ft.IconButton(ft.icons.ASSIGNMENT_IND_OUTLINED),
                            #label="Crear Cliente",
                            #on_click = lambda _: page.go("/registro_clientes")
                        #),
                        #ft.NavigationDrawerDestination(
                            ft.IconButton(ft.icons.LIST_ROUNDED, 
                                          tooltip="Listado de Clientes",
                                          on_click = lambda _: page.go("/listado_clientes")),
                            #selected_icon=ft.IconButton(ft.icons.ASSIGNMENT_IND_OUTLINED,on_click = lambda _: page.go("/listado_clientes")),
                            #label="Listado de Clientes",
                            #on_click = lambda _: page.go("/listado_clientes")
                        #),
                        #ft.NavigationDrawerDestination(
                            ft.IconButton(ft.icons.ADD_CIRCLE, 
                                          tooltip="Crear Registro",
                                          on_click = lambda _: page.go("/registros_diarios")),
                            #selected_icon=ft.Icon(ft.icons.ADD_CIRCLE_OUTLINE_OUTLINED),
                            #label="Crear Registro",
                            #on_click = lambda _: page.go("/registros_diarios")
                        #),
                        #ft.NavigationDrawerDestination(
                            ft.IconButton(ft.icons.DASHBOARD,
                                          tooltip="Dashboard",
                                          on_click = lambda _: page.go("/dashboard")),
                            #selected_icon=ft.Icon(ft.icons.DASHBOARD_OUTLINED),
                            #label="Dashboard",
                            #on_click = lambda _: page.go("/dashboard")
                        #),
                    ],
                    
                #     on_change=lambda e: print("selected destination: ", e.control.selected_index),
                #     ),
                #     ],
                # width=80,
                # height=700,
                # vertical_alignment=ft.CrossAxisAlignment.START
                ),
    # def on_destination_click(self, e):
    #     if e.control.label == "Crear Cliente":
    #         self.page.go("/registro_clientes")
    #     elif e.control.label == "Listado de Clientes":
    #         self.page.go("/listado_clientes")
    #     elif e.control.label == "Crear Registro":
    #         self.page.go("/registros_diarios")
    #     elif e.control.label == "Dashboard":
    #         self.page.go("/dashboard")
            
        
    # def abrir_drawer(self, e):
    #     self.page.drawer = self.sidebar
    #     self.sidebar.open = True
    #     self.page.update()
            
    )
    return sidebar
    
    


            
