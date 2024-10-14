import flet as ft

class Home(ft.UserControl):
    def  __init__(self, page):
        super().__init__(expand=True)
        self.page = page
        
        
    def build(self):
        return ft.Container(
            content=[
                ft.Text("Welcome to the home page"),
            ]
        )
