import flet as ft

class App(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.init_helper()
        
        def init_helper(self):
            self.pg.add(
                ft.Container(
                    expand=True,
                    bgcolor="blue",
                )
            )
            
def main(page: ft.Page):
    page.title = "sideBar ejemplo"
    aplication = App()
    page.add(aplication(page))
            
ft.app(target=App)