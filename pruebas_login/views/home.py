import flet as ft

class Home(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.expand = True
        self.bgcolor = "blue"
        
        self.content = ft.Text(
            "Welcome to my app soy el home",
        )
    
    def build(self):
        return self.content