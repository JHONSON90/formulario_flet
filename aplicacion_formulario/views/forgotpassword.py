import flet as ft 
from utils.validation import Validator
import re
import service.auth  as auth_service
class ForgotPassword(ft.UserControl):
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
                                "Olvidaste tu contraseña?",
                                size=16,
                                color='black',
                                text_align='center'
                            ),
                            ft.Text(
                                "No te preocupes nosotros enviamos un link para que puedas reestablecerla solo debes colocar tu correo electronico",
                                size=16,
                                color='black',
                                text_align='center'
                            ),
                            ft.Container(height=0),
                            
                            self.email_box,
                            
                            ft.Container(height=0),
                            
                            ft.Container(
                                alignment=ft.alignment.center,
                                bgcolor='#4e73df',
                                height=40,
                                border_radius=30,
                                content=ft.Text(
                                    "Reestablecer contraseña",
                                ),
                                on_click = self.reset_password
                            ),
                            ft.Container(height=0),
                            
                            ft.Container(
                                content=ft.Text(
                                    "Crear una cuenta",
                                    color='#4e73df',
                                    size=12
                                ),
                                on_click=lambda _:  self.page.go('/registro')
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
        self.email_box.content.value = ""
        self.update()
        
    def reset_password(self, e: ft.TapEvent):
        if not self.validator.is_valid_email(self.email_box.content.value):
            self.email_box.border = self.error_border
            print("entro en el if not del validador del correo")
            self.email_box.update()

        else:
            email = self.email_box.content.value
            print(f"soy el email del else {email}")
            self.page.controls.append(ft.ProgressRing()) 
            self.page.update()

            user = auth_service.reset_password(email)
            print(user)
            self.page.controls.remove(self.page.controls[-1])
            self.page.update()
            if user:
                self.page.overlay.append(ft.SnackBar(
                    ft.Text(
                        'Se ha enviado al correo las indicaciones para reestablecer tu contraseña.'),
                        open = True
                    )
                )
                self.clear_fields()
                self.page.update()
                self.page.go('/login')
            else:
                self.page.overlay.append(ft.SnackBar(
                    ft.Text(
                        'Correo invalido, Intenta nuevamente'), 
                    open=True
                    )
                )
                self.clear_fields()
                self.page.update()
            
    
    def build(self):
        return self.content