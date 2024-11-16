import flet as ft

class Dashboard(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.expand = True
        self.bgcolor = "blue"
        
        self.content = ft.Text(
            "estoy en el dashboard",
        )
    
    def build(self):
        return self.content