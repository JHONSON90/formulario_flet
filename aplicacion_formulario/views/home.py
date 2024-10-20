import flet as ft

class Login(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        self.alignment = ft.alignment.center
        
        
        self.email_box = ft.Container(
            content=ft.TextField(
                label= "Correo Electronico",
                value="",
                input_filter=ft.RegexInputFilter(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"),
                helper_text="Debe ser un correo electrónico válido",
                error_text="Formato de correo inválido",
                )
        )
        
        self.password = ft.Container(
            content=ft.TextField(
                label="Contraseña",
                password=True
            )
        ),
        
        self.form = ft.Column(
            alignment=ft.alignment.center,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    width=500,
                    border_radius=12,
                    padding=40,
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text("Bienvenido a tu aplicación",
                                    size=16,
                                    text_align="center"
                                    ),
                            self.email_box,
                            self.password,
                            
                            ft.Container(
                                alignment=ft.alignment.center,
                                height=40,
                                border_radius=30,
                                content=[
                                    ft.Text("Login")
                                ]
                            )
                        ]
                    )
                )
            ]
        )
        
        self.content = self.form
    
    def build(self):
        return self.content
    
    
"""
import flet as ft

# Componente de TextField con filtro de entrada basado en Regex para correo electrónico
email_field = ft.TextField(
    label="Correo electrónico",
    hint_text="Introduce tu correo electrónico",
    border_color="blue",
    input_filter=ft.RegexInputFilter(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"),
    helper_text="Debe ser un correo electrónico válido",
    error_text="Formato de correo inválido",
)

# Ejemplo básico de visualización
def main(page: ft.Page):
    page.title = "Validación de Correo Electrónico"
    
    def on_submit(e):
        if email_field.value == "":
            page.dialog = ft.AlertDialog(
                title=ft.Text("Error"),
                content=ft.Text("Por favor, ingrese un correo electrónico"),
                on_dismiss=lambda e: page.dialog.open = False,
            )
            page.dialog.open = True
        else:
            page.dialog = ft.AlertDialog(
                title=ft.Text("Correo Válido"),
                content=ft.Text(f"El correo {email_field.value} es válido"),
                on_dismiss=lambda e: page.dialog.open = False,
            )
            page.dialog.open = True
        page.update()

    submit_button = ft.TextButton("Validar correo", on_click=on_submit)

    # Añadir campo de correo y botón a la página
    page.add(email_field, submit_button)

ft.app(target=main)        
        
        """