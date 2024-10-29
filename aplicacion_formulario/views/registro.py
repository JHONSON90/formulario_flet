import flet as ft
import pyrebase
import datetime
from functools import partial
from views.home import auth

class Registro(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        self.alignment = ft.alignment.center
        
        self.nombres = ft.Container(
            content=ft.TextField(
                label= "Correo Electronico",
                value="",
                border="underline",
                prefix_icon=ft.icons.ACCOUNT_CIRCLE
                #input_filter=()
                )
        )
        
        self.email_box = ft.Container(
            content=ft.TextField(
                label= "Correo Electronico",
                value="",
                border="underline",
                prefix_icon=ft.icons.EMAIL
                #input_filter=()
                )
        )
        
        self.password = ft.Container(
            content=ft.TextField(
                label="Contraseña",
                border="underline",
                prefix_icon=ft.icons.LOCK,
                password=True,
                can_reveal_password=True
            )
        )
        
        self.password2 = ft.Container(
            content=ft.TextField(
                label="Confirmar Contraseña",
                border="underline",
                prefix_icon=ft.icons.LOCK,
                password=True,
                can_reveal_password=True
            )
        )
        
               
        self.registrarse = ft.Container(
            padding= ft.padding.only(20,20),
            content=ft.ElevatedButton(
                "Registrarse",
                width=280,
                on_click=partial(self.registro_usuario)
            )
        )
        self.iniciar_sesion = ft.Container(
            padding= ft.padding.only(20,20),
            content=ft.ElevatedButton(
                "Iniciar Sesion",
                width=280,
                on_click=lambda _: page.go("/")
            )
        )
        
        self.form = ft.Container(
            border_radius=20,
            width=320,
            height=500,
            bgcolor=ft.colors.PURPLE,
            padding=20,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                
                controls=[
                    ft.Container(
                        ft.Text(
                        "Registrarse",
                        width= 320,
                        weight="w900",
                        size=30,
                        text_align="center",                    
                            ),
                        padding=ft.padding.only(20,20)
                    ),
                self.nombres,
                self.email_box,
                self.password,
                self.password2,
                self.registrarse,
                self.iniciar_sesion         
                ]
                
            )
            
            )
        
        
        self.content = self.form
    
    def clear_fields(self):
        self.nombres.content.value = ""
        self.email_box.content.value = ""
        self.password.content.value = ""
        self.password2.content.value = ""
        self.update()
        
    def registro_usuario(self, e):
        email = self.email_box.content.value
        contraseña = self.password.content.value
        contraseña2 = self.password2.content.value
        
        if len(email) <= 0 and  len(contraseña) <= 0:
            print("Formulario Vacio")
            print(len(email), email)
            print(len(contraseña), contraseña)
            print(len(contraseña2), contraseña2)
        elif contraseña != contraseña2:
            print("Las contraseñas deben ser iguales")
        else:
            self.clear_fields()   
            try:
                auth.create_user_with_email_and_password(
                    email,
                    contraseña
            )
            except Exception as e:
                    print(e)
            
    
    def build(self):
        return self.content
  