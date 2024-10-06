import flet as ft
from seleccionar_fecha import  seleccionar_fecha
from peticiones import UserManager

class Formulario_Diario(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        page.padding = 0
        self.data = UserManager()
        self.expand=True
        self.alignment = ft.alignment.center
        self.error_border = ft.border.all(width=1,color="red")
        
        self.fecha = seleccionar_fecha()
        
        self.idClientes = ft.Container(
            content= ft.TextField(
                border=ft.InputBorder.NONE,
                content_padding= ft.padding.only(
                    top=0, bottom=0, right=20, left=20
                ),
                hint_style= ft.TextStyle(size=12,  color="#858796"),
                hint_text="Identificacion del cliente",
                cursor_color="#858796",
                text_style=ft.TextStyle(
                    size=14, 
                    color="black",
                ),
            ),
            border= ft.border.all(width=1, color="#bdcbf4"),
            border_radius=20
        )    
        
        self.nombres = ft.Container(
            content= ft.TextField(
                #TODO: COLOCAR POR DEFAULT EL VALOR QUE TRAE LA IDENTIFICACION DEL USUARIO DEL ANTERIOR TEXTFIELD
                border=ft.InputBorder.NONE,
                content_padding= ft.padding.only(
                    top=0, bottom=0, right=20, left=20
                ),
                hint_style= ft.TextStyle(size=12,  color="#858796"),
                hint_text="Nombre del cliente",
                cursor_color="#858796",
                text_style=ft.TextStyle(
                    size=14, 
                    color="black",
                ),
            ),
            border= ft.border.all(width=1, color="#bdcbf4"),
            border_radius=20
        )    
        
        self.usuario_final = ft.Container(
            content= ft.TextField(
                border=ft.InputBorder.NONE,
                content_padding= ft.padding.only(
                    top=0, bottom=0, right=20, left=20
                ),
                hint_style= ft.TextStyle(size=12,  color="#858796"),
                hint_text="A quien se le consigna?",
                cursor_color="#858796",
                text_style=ft.TextStyle(
                    size=14, 
                    color="black",
                ),
            ),
            border= ft.border.all(width=1, color="#bdcbf4"),
            border_radius=20
        ) 
        
        self.tipo_de_servicio = ft.Container(
            content= ft.TextField(
                border=ft.InputBorder.NONE,
                content_padding= ft.padding.only(
                    top=0, bottom=0, right=20, left=20
                ),
                hint_style= ft.TextStyle(size=12,  color="#858796"),
                hint_text="Tipo de transaccion",
                cursor_color="#858796",
                text_style=ft.TextStyle(
                    size=14, 
                    color="black",
                ),
            ),
            border= ft.border.all(width=1, color="#bdcbf4"),
            border_radius=20
        )       
        
        self.valor = ft.Container(
            content= ft.TextField(
                border=ft.InputBorder.NONE,
                content_padding= ft.padding.only(
                    top=0, bottom=0, right=20, left=20
                ),
                hint_style= ft.TextStyle(size=12,  color="#858796"),
                hint_text="Valor recibido",
                cursor_color="#858796",
                text_style=ft.TextStyle(
                    size=14, 
                    color="black",
                ),
            ),
            border= ft.border.all(width=1, color="#bdcbf4"),
            border_radius=20
        )      
        
        self.valor_del_servicio = ft.Container(
            content= ft.TextField(
                border=ft.InputBorder.NONE,
                content_padding= ft.padding.only(
                    top=0, bottom=0, right=20, left=20
                ),
                hint_style= ft.TextStyle(size=12,  color="#858796"),
                hint_text="Cuanto le cobra al cliente por la transaccion?",
                cursor_color="#858796",
                text_style=ft.TextStyle(
                    size=14, 
                    color="black",
                ),
            ),
            border= ft.border.all(width=1, color="#bdcbf4"),
            border_radius=30
        )      
    
    
        self.conent = ft.Column(
            alignment= "center",
            horizontal_alignment= "center",
            controls=[
                ft.Container(
                    width=500,
                    border_radius=12,
                    padding= 40,
                    bgcolor="white",
                    content= ft.Column(
                        horizontal_alignment="center",
                        controls=[
                            ft.Text(
                                "Registro de Transacciones",
                                size=16,
                                color="black",
                                text_align="center"
                            ),
                            self.fecha, 
                            self.idClientes,
                            self.nombres,
                            self.tipo_de_servicio,
                            self.usuario_final,
                            self.valor,
                            self.valor_del_servicio,
                        ]
                    )
                )
            ]
        )
        
    
    def build(self):
        return self.conent
        
        
def main(page: ft.Page):
    page.title = "Formulario de Registro"
    page.bgcolor = "black"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.update()
    page.window.min_height = 500
    page.window.min_width = 100
    page.add(Formulario_Diario(page))
    


ft.app(main)