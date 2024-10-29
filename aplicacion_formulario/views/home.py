import flet as ft
import pyrebase
import datetime
from functools import partial


config = {
    "apiKey": "AIzaSyBEkRXhhYWcZ4ZotXKt5fpAJnAXhK-Hi6Q",
    "authDomain": "formulario-transacciones.firebaseapp.com",
    "projectId": "formulario-transacciones",
    "storageBucket": "formulario-transacciones.appspot.com",
    "messagingSenderId": "327051591986",
    "appId": "1:327051591986:web:4a08ae30e52fd6a812d72b",
    "databaseURL": ""
        #"https://formulario-transacciones-default-rtdb.firebaseio.com",
  };

#inicializar firebase
firebase = pyrebase.initialize_app(config)

# set up authentication manager

auth = firebase.auth()

class AppState:
    def __init__(self):
        self.user = None
app_state = AppState()


class Login(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        self.alignment = ft.alignment.center
        
        
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
        
        self.recuerdame = ft.Container(
            padding= ft.padding.only(80),
            content=ft.Checkbox(
                label="Recordar Contraseña"
                )
        )
        
        self.iniciar_sesion = ft.Container(
            padding= ft.padding.only(20,20),
            content=ft.ElevatedButton(
                "INICIAR",
                width=280, 
                on_click=partial(self.sign_in)
            )
        )
        self.registrarse = ft.Container(
            padding= ft.padding.only(20,20),
            content=ft.ElevatedButton(
                "REGISTRARSE",
                width=280, 
                on_click=lambda _: page.go("/registro")
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
                        "Iniciar  Sesión",
                        width= 320,
                        weight="w900",
                        size=30,
                        text_align="center",                    
                            ),
                        padding=ft.padding.only(20,20)
                    ),

                self.email_box,
                self.password,
                self.recuerdame,
                self.iniciar_sesion,
                self.registrarse
                ]
                
            )
            
            )
        
        self.content = self.form
    
    def clear_fields(self):
        self.email_box.content.value = ""
        self.password.content.value = ""
        self.update()
        
    
    def sign_in(self, e):
        email = self.email_box.content.value
        contraseña = self.password.content.value 
        
        if not email or not  contraseña:
            print("Favor ingrese todos los campos")
            return False
            
        try:
            user = auth.sign_in_with_email_and_password(
                   email,
                   contraseña
                )
            info = auth.get_account_info(user["idToken"])
                
            if info:
                    app_state.user = user
                    self.clear_fields()
                    print("entro y estoy aqui")
                    self.page.go("/home")
                    print("paso y estoy aqui")
                    print(app_state.user)
                    return True

            else: return  False
            
    
                
        except Exception as e:
                print(f"Favor verifique los datos ingresados{e}")
                return False
    
    def build(self):
        return self.content
  