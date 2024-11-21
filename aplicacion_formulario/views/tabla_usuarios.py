import flet as ft
from data.peticiones import UserManager

class Tabla_datos_clientes(ft.UserControl):
    def __init__(self, page):
        super().__init__(expand=True)
        self.page = page
        page.bgcolor = ft.colors.INDIGO_50
        self.data = UserManager()
        self.selected_row = None
        
        self.search_filed = ft.TextField(
            label="Nombre",
            value="",
            suffix_icon=ft.icons.SEARCH,
            border= ft.InputBorder.UNDERLINE,
            #border_color="white",
            #label_style=ft.TextStyle(color="white"),
            #color="white",
            on_change= self.search_data,
        )
        
        self.data_table = ft.DataTable(
            expand=True,
            border=ft.border.all(2, color="#858796"),
            border_radius=10,
            column_spacing=30,
            
            show_checkbox_column=True,
            # data_row_color={
            #     ft.ControlState.SELECTED:"gray",
            #     ft.ControlState.PRESSED:"gray"
            # },
            columns=[
                ft.DataColumn(ft.Text("Identificacion", weight="bold"),                        numeric=True),
                ft.DataColumn(ft.Text("Nombres y Apellidos", weight="bold")),
                ft.DataColumn(ft.Text("Telefono", weight="bold"), numeric=True),
                ft.DataColumn(ft.Text("Correo Electronico", weight="bold")),
            ]
        )
        
        self.show_data()
        
        
        self.table =  ft.Container(
            #bgcolor="#858796",
            border_radius=10,
            padding=10,
            col=5,
            
            content=ft.Column(
                expand=True,
                controls=[
                    ft.Container(
                        #padding=10,
                        content=ft.Row(
                            scroll="always",
                            controls=[
                                self.search_filed,   
                            ]
                        )
                    ),
                    ft.Container(height=0),
                    ft.Column(
                        expand=True,
                        scroll="auto",
                        
                        controls=[
                            ft.ResponsiveRow(adaptive=True,
                                             controls=[
                                self.data_table,                                
                            ])
                        ]
                    )
                ]
            )
        )
        
        self.content = self.table

        
    def show_data(self):
        self.data_table.rows=[]
        for x in self.data.get_users():
            self.data_table.rows.append(
                ft.DataRow(
                    on_select_changed=self.get_index,
                    cells=[
                        ft.DataCell(ft.Text(str(x[0]))),
                        ft.DataCell(ft.Text(x[1])),
                        ft.DataCell(ft.Text(str(x[2]))),
                        ft.DataCell(ft.Text(x[3])),
                    ]
                )
            )
        self.update()
        
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
                                ft.DataCell(ft.Text(str(x[0]))),
                                ft.DataCell(ft.Text(x[1],)),
                                ft.DataCell(ft.Text(str(x[2]),)),
                                ft.DataCell(ft.Text(x[3],)),
                            ]
                        )
                    )
                    self.update()
        else:
            self.show_data()
            
    def build(self):
        return self.content