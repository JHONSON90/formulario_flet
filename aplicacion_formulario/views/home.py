import flet as ft
from utils.validation import Validator
import re
from service.auth import login_user, store_session

class Login(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        page.padding = 0
        self.validator = Validator()
        self.expand = True
        self.bgcolor = "#4e73df"
        self.alignment = ft.alignment.center
        
        self.error_border = ft.border.all(width=1, color="red")
        
        self.email_box = ft.Container(
            content= ft.TextField(
                border= ft.InputBorder.NONE,
                content_padding = ft.padding.only(
                    top=0,bottom=0, right=20, left=20
                ),
                hint_style= ft.TextStyle(
                    size=12,
                    color="#858796"
                ),
                hint_text = "Correo Electronico...",
                cursor_color = "#858796",
                text_style = ft.TextStyle(
                    size=14,
                    color="black"
                ),
            ),
            border= ft.border.all(width=1, color="#bdcbf4"),
            border_radius = 20
        )
        
        self.password_box = ft.Container(
            content= ft.TextField(
                border= ft.InputBorder.NONE,
                content_padding = ft.padding.only(
                    top=0,bottom=0, right=20, left=20
                ),
                hint_style= ft.TextStyle(
                    size=12,
                    color="#858796"
                ),
                hint_text = "Contraseña...",
                cursor_color = "#858796",
                text_style = ft.TextStyle(
                    size=14,
                    color="black"
                ),
            ),
            border= ft.border.all(width=1, color="#bdcbf4"),
            border_radius = 20
        )
        
        self.form = ft.Column(
            alignment = "center",
            horizontal_alignment = "center",
            controls=[
                ft.Container(
                    width=500,
                    border_radius=12,
                    padding=40,
                    bgcolor='white',
                    content= ft.Column(
                        horizontal_alignment='center',
                        controls=[
                            ft.Text(
                                "Bienvenido!!!",
                                size=16,
                                color='black',
                                text_align='center'
                            ),
                            self.email_box,
                            
                            self.password_box,
                            ft.Container(height=0),
                            
                            ft.Container(
                                alignment=ft.alignment.center,
                                bgcolor='#4e73df',
                                height=40,
                                border_radius=30,
                                content=ft.Text(
                                    "Iniciar Sesión",
                                ),
                                on_click = self.login
                            ),
                            ft.Container(height=0),
                            
                            ft.Container(
                                content=ft.Text(
                                    "¿Olvidaste tu contraseña?",
                                    color='#4e73df',
                                    size=12
                                ),
                                on_click=lambda _: (
                                    setattr(self.page, 'data', self.email_box.content.value), self.page.go('/forgotpassword'))
                            ),
                            ft.Container(
                                content=ft.Text(
                                    "Crear nuevo usuario",
                                    color='#4e73df',
                                    size=12
                                ),
                                on_click=lambda _: (
                                    self.page.go('/registro'))
                            ),
                            
                        ]
                    )
                    
                )
            ]
        )        
        self.content = self.form
    
    def clear_fields(self):
        self.email_box.content.value = ""
        self.password.content.value = ""
        self.update()
        
    def login(self, e):
        if not self.validator.is_valid_email(self.email_box.content.value):
            self.email_box.border = self.error_border
            self.email_box.update()

        if not self.validator.is_valid_password(self.password_box.content.value):
            self.password_box.border = self.error_border
            self.password_box.update()

        else:
            email = self.email_box.content.value
            password = self.password_box.content.value

            self.page.controls.append(ft.ProgressBar()) 
            self.page.update()

            token = login_user(email, password)
            self.page.splash = None
            self.page.update()
            if token:
                store_session(token)
                self.page.go('/me')
            else:
                self.page.snack_bar = ft.SnackBar(
                    ft.Text('Invalid credentials')
                )
                self.page.snack_bar.open = True
                self.page.update()
    
    
    def build(self):
        return self.content
  