import flet as ft
from ..seleccionar_fecha import  seleccionar_fecha
from ..peticiones import UserManager

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
                input_filter=ft.NumbersOnlyInputFilter(),
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
                input_filter=ft.NumbersOnlyInputFilter(),
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
                input_filter=ft.NumbersOnlyInputFilter(),
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
                            ft.Container(
                                content=ft.Row(
                                    alignment= ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.TextButton(
                                        ft.Text="Guardar",
                                        icon=ft.icons.SAVE,
                                        style=ft.ButtonStyle(
                                        color="white",
                                    ),
                                    on_click= self.add_data
                                    ),
                                        ],
                                    ),
                            )
                        ]
                    )
                )
            ]
        )
        
        self.formulario_vacio = ft.AlertDialog(
            modal=True,
            title="Error",
            content="El formulario esta  vacio",
            actions=ft.TextButton("Ok", on_click=self.close_dlg),
            actions_alignment=ft.MainAxisAlignment.END,
        )
        
    def close_dlg(self, e):
        self.formulario_vacio.open =  False,
        e.contol.page.update()

    
    def build(self):
        return self.conent
    
    def clean_fields(self):
        self.idClientes = ""
        self.nombres = ""
        self.tipo_de_servicio = ""
        self.usuario_final = ""
        self.valor = ""
        self.valor_del_servicio = ""
        self.fecha = ""
    
    
    
    def add_data(self, e):
        idClientes = self.idClientes.value,
        fecha = "2024-04-20 ",
        tipo_de_servicio = self.tipo_de_servicio,
        usuario_final= self.usuario_final,
        valor = self.valor,
        valor_del_servicio = self.valor_del_servicio,
    
        if idClientes != "" and  fecha != "" and tipo_de_servicio != "" and usuario_final != "" and valor != "" and  valor_del_servicio != "":
            print("formulario vacio")
        else:
            self.clean_fields()
            self.data.add_registros(idClientes,  fecha, tipo_de_servicio, usuario_final, valor, valor_del_servicio),

            

        
def main(page: ft.Page):
    page.title = "Formulario de Registro"
    page.bgcolor = "black"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.update()
    page.window.min_height = 500
    page.window.min_width = 100
    page.add(Formulario_Diario(page))
    


ft.app(main)