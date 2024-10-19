import flet as ft
from views.sidebar import my_Sidebar

class Home(ft.UserControl):
    def __init__(self, page):
        super().__init__(expand=True)        
        self.page = page
        
        self.home = ft.Column(
        controls= [
            ft.Text("Welcome my page", 
                    color=ft.colors.CYAN_100,
                    size=50)
        ])
        
        self.content = ft.Row(
            controls=[
                my_Sidebar(page),
                self.home
            ]
        )
        
    def build(self):
        return self.content
        
