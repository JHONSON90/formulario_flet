import flet as ft
from utils.validation import Validator
import re
from service.auth import *

class Registro(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        page.padding = 0
        self.validator = Validator()
        self.expand = True
        self.bgcolor = "#4e73df"
        self.alignment = ft.alignment.center
        
        self.error_border = ft.border.all(width=1, color="red")
        
        self.name_box = ft.Container(
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
                                "Crear una cuenta",
                                size=16,
                                color='black',
                                text_align='center'
                            ),
                            ft.Container(height=0),
                            
                            self.name_box,
                            self.email_box,
                            self.password_box,
                            
                            ft.Container(height=0),
                            
                            ft.Container(
                                alignment=ft.alignment.center,
                                bgcolor='#4e73df',
                                height=40,
                                border_radius=30,
                                content=ft.Text(
                                    "Crear Cuenta",
                                ),
                                on_click = self.signup
                            ),
                            ft.Container(height=0),
                            
                            ft.Container(
                                content=ft.Text(
                                    "¿Olvidaste tu contraseña?",
                                    color='#4e73df',
                                    size=12
                                ),
                                on_click=lambda _:  self.page.go('/forgotpassword')
                            ),
                            ft.Container(
                                content=ft.Text(
                                    "Ya tienes una cuenta? Ir a iniciar sesión",
                                    color='#4e73df',
                                    size=12
                                ),
                                on_click=lambda _: (
                                    self.page.go('/login'))
                            ),
                            
                        ]
                    )
                    
                )
            ]
        )
        
        
        self.content = self.form
    
    def clear_fields(self):
        self.nombres.content.value = ""
        self.email_box.content.value = ""
        self.password.content.value = ""
        self.password2.content.value = ""
        self.update()
        
    def signup(self, e):
        if not self.validator.validate_name(self.name_box.content.value):
            self.name_box.border = self.error_border
            self.name_box.update()

        if not self.validator.is_valid_email(self.email_box.content.value):
            self.email_box.border = self.error_border
            self.email_box.update()

        if not self.validator.is_valid_password(self.password_box.content.value):
            self.password_box.border = self.error_border
            self.password_box.update()

        else:
            name = self.name_box.content.value
            email = self.email_box.content.value
            password = self.password_box.content.value

            print(name, email, password)
            self.page.controls.append(ft.ProgressRing())
            self.page.update()

            user = create_user(name, email, password)
            if user:
                token = login_user(email, password)
                store_session(token)
            self.page.controls.remove(self.page.controls[-1])
            self.page.update()
            self.page.go('/login')
            
    def input_on_focus(self, e):
        e.control.border = ft.border.all(width=1, color='#bdcbf4')
        e.control.update()
    
    def build(self):
        return self.content
  