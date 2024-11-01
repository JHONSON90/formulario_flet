import flet as ft
from datetime import datetime
from data_base.peticiones import UserManager
from views.sidebar import my_Sidebar

class Formulario_Diario(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        page.padding = 0
        self.data = UserManager()
        self.expand=True
        self.alignment = ft.alignment.center
        self.error_border = ft.border.all(width=1,color="red")
        
        self.fecha_actual = datetime.now().strftime("%Y-%m-%d")
        
        self.idClientes = ft.TextField(
                value="",
                border_color="white",
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
   
        
        self.nombres = ft.TextField(
                value="",
                read_only=True,
                border_color="white",
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
   
        
        self.usuario_final = ft.TextField(
                value="",
                border_color="white",
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
           
        
        self.tipo_de_servicio = ft.TextField(
                value="",
                border_color="white",
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
     
        
        self.valor = ft.TextField(
                value="",
                border_color="white",
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
                 
        
        self.valor_del_servicio = ft.TextField(
                value="",
                border_color="white",
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
        
        self.form_registro_clientes = ft.Column(
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
                                ft.Row(
                                        alignment= ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.TextButton(
                                                "Guardar",
                                                icon=ft.icons.SAVE,
                                        on_click= self.add_data
                                        ),
                                            ],
                                        ),
                            ],
                            
                                    )
            
                # )]
            # #     #             )
            # ]
            #             )                
    
    
        self.conent = ft.Row(
            controls= [
                my_Sidebar(page),
                self.form_registro_clientes
            ]
        )
                # ft.Column(
                #     alignment= "center",
                #     horizontal_alignment= "center",
                #     controls=[
                #         ft.Container(
                #             width=500,
                #             border_radius=12,
                #             padding= 40,
                #             #bgcolor="white",
                            #content= 
            #                 ft.Column(
            #                 horizontal_alignment="center",
            #                 controls=[
            #                     ft.Text(
            #                         "Registro de Transacciones",
            #                         size=16,
            #                         #color="black",
            #                         text_align="center"
            #                     ),                            
            #                     self.idClientes,
            #                     self.nombres,
            #                     self.tipo_de_servicio,
            #                     self.usuario_final,
            #                     self.valor,
            #                     self.valor_del_servicio,
            #                     ft.Row(
            #                             alignment= ft.MainAxisAlignment.CENTER,
            #                             controls=[
            #                                 ft.TextButton(
            #                                     "Guardar",
            #                                     icon=ft.icons.SAVE,
            #                             on_click= self.add_data
            #                             ),
            #                                 ],
            #                             ),
            #                 ],
                            
            #                         )
            
            #     # )]
            # #     #             )
            # ]
            #             )
        
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
        self.idClientes.value = ""
        self.nombres.value = ""
        self.tipo_de_servicio.value = ""
        self.usuario_final.value = ""
        self.valor.value = ""
        self.valor_del_servicio.value = ""
        
    
    
    
    def add_data(self, e):
        idClientes = self.idClientes.value 
        valor = self.valor.value
        fecha = self.fecha_actual.value
        valor_del_servicio = self.valor_del_servicio.value
        tipo_de_servicio = self.tipo_de_servicio.value
        usuario_final= self.usuario_final.value
        
        if idClientes == "" and  tipo_de_servicio == "" and usuario_final == "" and valor == "" and  valor_del_servicio == "":
            print("formulario vacio")
        else:
            self.clean_fields()
            self.data.add_registros(idClientes, valor,  fecha, valor_del_servicio, tipo_de_servicio, usuario_final),
            self.update()
            
    def busqueda_nombre(self, e):
        id_Cliente =  self.idClientes.value
        nombre = self.data.get_user(id_Cliente)
                
        if nombre:
            self.nombres.value = nombre
        else:
            self.nombres.value = "Cliente no encontrado"
        
        self.update()
        
x = UserManager()
# print(x.get_user(1085917679))

from datetime import datetime

hoy = datetime.now().strftime("%Y-%m-%d")

x.add_registros(1085917679,  100, hoy, 100, "prueba2", "prueba2")