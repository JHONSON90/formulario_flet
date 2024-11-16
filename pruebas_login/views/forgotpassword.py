import flet as ft

class ForgotPassword(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.expand = True
        self.bgcolor = "blue"
        
        self.content = ft.Text(
            "olvide la contraseña",
        )
    
    def build(self):
        return self.content