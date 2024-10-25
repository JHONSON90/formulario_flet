import flet as ft

class Login(ft.Container):
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
                width=280
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
                self.iniciar_sesion
                
                ]
                
            )
            
            )
        
        self.content = self.form
    
    def build(self):
        return self.content
  