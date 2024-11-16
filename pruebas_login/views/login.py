import flet as ft

class Login(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.expand = True
        self.bgcolor = "blue"
        
        self.content = ft.Text(
            "Estoy en el login",
        )
    
    def build(self):
        return self.content