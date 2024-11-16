import flet as ft

class Signup(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.expand = True
        self.bgcolor = "blue"
        
        self.content = ft.Text(
            "Crear usuario",
        )
    
    def build(self):
        return self.content