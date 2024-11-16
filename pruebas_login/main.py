import flet as ft
from views.dashboard import Dashboard
from views.forgotpassword import ForgotPassword
from views.login import Login
from views.singup import Signup
from views.home import Home



class Main(ft.UserControl):
    def __init__(self, page: ft.Page,):
        super().__init__()
        page.padding = 0
        self.page = page
        self.init_helper()

    def init_helper(self):
        self.page.on_route_change = self.on_route_change
        self.page.go("/login")
        
    def on_route_change(self, e: ft.RouteChangeEvent): #1:13
        def view_pop(view):
            if len(self.page.views) > 1:
                self.page.views.pop()
                top_view = self.page.views[-1]
                self.page.go(top_view.route)
                
        view_pop(self.page.views[-1])
        
        new_page = {
            "/": Home,
            "/login": Login,
            "/signup": Signup,
            "/me": Dashboard,
            "/forgotpassword": ForgotPassword

        }[e.route](self.page)

        self.page.views.clear()
        self.page.views.append(
            ft.View(e.route, [new_page])
        )
        self.page.update()

ft.app(target=Main)