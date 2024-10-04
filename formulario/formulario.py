import flet as ft
import datetime
from peticiones import UserManager

class Formulario(ft.Column):
    def __init__(self, page):
        super().__init__(expand=True)
        
        self.page = page
        self.data = UserManager()
        self.selected_row = None
        
#region=: TEXT FIELDS DE LOS 4  CAMPOS

        self.idClientes = ft.TextField(value="",
                                 label="Identificacion",
                                 border_color="white",
                                 input_filter=ft.NumbersOnlyInputFilter(),
                                 )
        
        self.nombres = ft.TextField(value="",
                                 label="Nombres",
                                 border_color="white")
        
        self.telefono = ft.TextField(value="",
                                 label="Telefono",
                                 border_color="white",
                                 input_filter=ft.NumbersOnlyInputFilter()
                                 )
        
        self.correo = ft.TextField(value="",
                                 label="Correo",
                                 border_color="white")
        
       
        self.search_filed = ft.TextField(
            label="Nombre",
            value="",
            suffix_icon=ft.icons.SEARCH,
            border= ft.InputBorder.UNDERLINE,
            border_color="white",
            label_style=ft.TextStyle(color="white"),
            color="white",
            on_change= self.search_data,
        )
        
        self.data_table = ft.DataTable(
            expand=True,
            border=ft.border.all(2,"white"),
            border_radius=10,
            show_checkbox_column=True,
           
            # data_row_color={
            #     ft.ControlState.SELECTED:"gray",
            #     ft.ControlState.PRESSED:"gray"
            # },
            columns=[
                ft.DataColumn(ft.Text("Identificacion", color="white", weight="bold"),                             
                              numeric=True),
                ft.DataColumn(ft.Text("Nombres y Apellidos", color="white", weight="bold")),
                
                ft.DataColumn(ft.Text("Telefono", color="white", weight="bold"), numeric=True),
                
                ft.DataColumn(ft.Text("Correo Electronico", color="white", weight="bold")),
                
            ]
        )
        
        self.show_data()
        
        self.form = ft.Container(
            bgcolor="#222222",
            border_radius=10,
            col=4,
            height="auto",
            padding=10,
            content=ft.Column(
                alignment= ft.MainAxisAlignment.CENTER,
                horizontal_alignment= ft.CrossAxisAlignment.CENTER,

                controls=[
                    ft.Text(
                        "Formulario de Registro",
                        size=40,
                        text_align="center",
                        color="white",
                    ),
                    self.idClientes,
                    self.nombres,
                    self.telefono,
                    self.correo,
                    ft.Container(
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.TextButton(
                                    text="Guardar",
                                    icon=ft.icons.SAVE,
                                    style=ft.ButtonStyle(
                                        color="white",
                                    ),
                                    on_click=self.add_data
                                )
                            ]
                        )
                    )
                ]
            )
        )
        
        self.table =  ft.Container(
            bgcolor="#222222",
            border_radius=10,
            padding=10,
            col=6,
            content=ft.Column(
                #expand=True,
                controls=[
                    ft.Container(
                        padding=10,
                        content=ft.Row(
                            scroll="always",
                            controls=[
                                self.search_filed,
                                
                            ]
                        )
                    ),
                    ft.Column(
                        expand=True,
                        scroll="always",
                        
                        controls=[
                            ft.ResponsiveRow([
                                self.data_table,
                                
                            ])
                        ]
                    )
                ]
            )
        )

              
        self.conent = ft.ResponsiveRow(
            controls=[
                self.form,
                self.table
            ]
        )
        
    def show_data(self):
        self.data_table.rows=[]
        for x in self.data.get_users():
            self.data_table.rows.append(
                ft.DataRow(
                    on_select_changed=self.get_index,
                    cells=[
                        ft.DataCell(ft.Text(str(x[0]), color="white")),
                        ft.DataCell(ft.Text(x[1], color="white")),
                        ft.DataCell(ft.Text(str(x[2]), color="white")),
                        ft.DataCell(ft.Text(x[3], color="white")),
                    ]
                )
            )
        self.update()
        
    def add_data(self, e):
        idClientes = self.idClientes.value
        nombres = self.nombres.value
        telefono = self.telefono.value
        correo = self.correo.value
        
        if idClientes != "" and nombres !=  "" and telefono != "" and correo != "":
            user_exist= False
            for row in self.data.get_users():
                if row[0] == idClientes:
                    user_exist = True
                    break
                if not user_exist:
                    self.clean_fields()
                    self.data.add_users(idClientes,nombres,telefono, correo),
                    self.show_data()
    
    def get_index(self, e):
        if e.control.selected:
            e.control.selected = False
        else:
            e.control.selected = True
            
        nombres = e.control.cells[1].content.value
        for row in self.data.get_users():
            if row[1] == nombres:
                self.selected_row = row
                break
        self.update()
        
    def edit_filed_text(self, e):
        try:
            self.idClientes.value = self.selected.row[0]
            self.nombres.value = self.selected.row[1]
            self.telefono.value = self.selected.row[2]
            self.correo.value = self.selected_row[3]
            self.update()
        except TypeError:
            print("Error")
        
    def search_data(self, e):
        search = self.search_filed.value.lower()
        nombres_buscados = list(filter(lambda x: search in x[1].lower(), self.data.get_users()))
        self.data_table.rows= []
        if not self.search_filed.value == "":
            if len(nombres_buscados)>0:
                for x in nombres_buscados:
                    self.data_table.rows.append(
                        ft.DataRow(
                            on_select_changed= self.get_index,
                            cells=[
                                ft.DataCell(ft.Text(str(x[0]), color="white")),
                                ft.DataCell(ft.Text(x[1],  color="white")),
                                ft.DataCell(ft.Text(str(x[2]),  color="white")),
                                ft.DataCell(ft.Text(x[3],  color="white")),

                            ]
                        )
                    )
                    self.update()
        else:
            self.show_data()
                               

    
    def clean_fields(self):
        self.idClientes.value = ""
        self.nombres.value = ""
        self.telefono.value = ""
        self.correo.value = ""
        self.show_data()
        
        
    def build(self):
        return self.conent
        

        
def main(page: ft.Page):
    page.title = "Formulario de Registro"
    page.bgcolor = "black"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.update()
    page.window.min_height =1100
    page.window.min_width =500
    page.add(Formulario(page))


ft.app(main)