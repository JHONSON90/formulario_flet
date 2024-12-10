import flet as ft 

class MenuHome(ft.UserControl):
    def __init__(self):
        super().__init__()
        
        self.peticion = ft.Card(
            width=400,
            content= ft.Column(
                #padding = 10,
                controls=[
                ft.Icon(ft.icons.NAVIGATE_NEXT_OUTLINED),
                ft.Container(height=20),
                ft.Text("PETICIÓN.", size=20, weight=ft.FontWeight.BOLD),
                ft.Text("Son solicitudes formales que se hacen a una entidad para que realice alguna acción o gestión un trámite.")
                
                ]
            )
        )
        
        self.queja = ft.Card(
            #padding = 10,
            width=400,
            content= ft.Column(
                controls=[
                ft.Icon(ft.icons.NAVIGATE_NEXT_OUTLINED),
                ft.Container(height=20),
                ft.Text("QUEJA.", size=20, weight=ft.FontWeight.BOLD),
                ft.Text("Expresan el descontento de una persona frente a un servicio o producto que no cumple con lo esperado.")
                ]
            )
        )
        
        self.reclamo = ft.Card(
            #padding = 10,
            width=400,
            content= ft.Column(
                controls=[
                ft.Icon(ft.icons.NAVIGATE_NEXT_OUTLINED),
                ft.Container(height=20),
                ft.Text("RECLAMO.", size=20, weight=ft.FontWeight.BOLD),
                ft.Text("Son solicitudes formales para que se corrija una situación que causa un perjuicio o daño.")
                ]
            )
        )
        
        self.sugerencia = ft.Card(
            #padding = 10,
            width=400,
            content= ft.Column(
                controls=[
                ft.Icon(ft.icons.NAVIGATE_NEXT_OUTLINED),
                ft.Container(height=20),
                ft.Text("SUGERENCIA.", size=20, weight=ft.FontWeight.BOLD),
                ft.Text("Son propuestas para mejorar un servicio o producto.")
                ]
            )
        )
        
        self.felicitacion = ft.Card(
            #padding = 10,
            width=400,
            content= ft.Column(
                controls=[
                ft.Icon(ft.icons.NAVIGATE_NEXT_OUTLINED),
                ft.Container(height=20),
                ft.Text("FELICITACIONES.", size=20, weight=ft.FontWeight.BOLD),
                ft.Text("Es una forma de reconocer y valorar el buen trabajo realizado, la atención de calidad o la solución efectiva a una solicitud o problema.")
                ]
            )
        )
        
    def build(self):
        return ft.Container(
            width="auto",
            padding=10,
            content= ft.Column(
                controls=[
                ft.Row(
                    controls=[
                        self.queja,
                        self.reclamo,
                        self.peticion
                    ],
                ),
                ft.Row(
                        controls=[
                            self.sugerencia,
                            self.felicitacion
                        ]
                    )
                ]
            )
        )
        