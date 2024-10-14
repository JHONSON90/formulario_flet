import flet as ft
from data_base.peticiones import UserManager
from datetime import datetime


class Formulario_Diario(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        page.padding = 0
        self.data = UserManager()
        self.expand=True
        self.alignment = ft.alignment.center
        self.error_border = ft.border.all(width=1,color="red")
        
        self.fecha_actual = datetime.now().strftime("%Y-%m-%d")
        
        self.idClientes = ft.Container(
            content= ft.TextField(
                value="",
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
                on_blur=self.busqueda_nombre
            ),
            border= ft.border.all(width=1, color="#bdcbf4"),
            border_radius=20
        )    
        
        self.nombres = ft.Container(
            content= ft.TextField(
                value="",
                read_only=True,
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
                value="",
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
                value="",
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
                value="",
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
                value="",
                border=ft.InputBorder.NONE,
                content_padding= ft.padding.only(
                    top=0, bottom=0, right=20, left=20
                ),
                hint_style= ft.TextStyle(size=12),  #color="#858796"),
                hint_text="Cuanto le cobra al cliente por la transaccion?",
                # cursor_color="#858796",
                text_style=ft.TextStyle(
                    size=14, 
                    #color="black",
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
                    #bgcolor="white",
                    content= ft.Column(
                        horizontal_alignment="center",
                        controls=[
                            ft.Text(
                                "Registro de Transacciones",
                                size=16,
                                #color="black",
                                text_align="center"
                            ),                            
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
                                            "Guardar",
                                            icon=ft.icons.SAVE,
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
        idClientes = self.idClientes.content.value
        valor = self.valor
        fecha = self.fecha_actual
        valor_del_servicio = self.valor_del_servicio
        tipo_de_servicio = self.tipo_de_servicio
        usuario_final= self.usuario_final
        
        print(idClientes, valor)
    
        if idClientes == "" and  tipo_de_servicio == "" and usuario_final == "" and valor == "" and  valor_del_servicio == "":
            print("formulario vacio")
        else:
            self.clean_fields()
            self.data.add_registros(idClientes, valor,  fecha, valor_del_servicio, tipo_de_servicio, usuario_final),
            
    def busqueda_nombre(self, e):
        id_Cliente =  self.idClientes.content.value
        nombre = self.data.get_user(id_Cliente)
        
        if nombre:
            self.nombres.content.value = nombre
        else:
            self.nombres.content.value = "Cliente no encontrado"
        
        self.update()