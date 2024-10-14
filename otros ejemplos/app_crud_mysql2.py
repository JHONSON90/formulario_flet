import flet as ft
from db_conect2 import UserManager

class Form(ft.UserControl):
    def __init__(self, page):
        super().__init__(expand=True)

        self.page = page
        self.data = UserManager()

        self.name= ft.TextField(value="", label="Nombre", label_style= ft.TextStyle(color= "white"), border_color="purple", color="white")

        self.age= ft.TextField(value="", label="Edad", label_style= ft.TextStyle(color= "white"), border_color="purple", color="white",
                                input_filter= ft.NumbersOnlyInputFilter(),
                                                    max_length=2)
        self.search_filed= ft.TextField(
            label="Buscar por nombre",
            suffix_icon= ft.icons.SEARCH,
            border= ft.InputBorder.UNDERLINE,
            border_color="white",
            label_style= ft.TextStyle(color= "white"),
            color= "white"
        )


        self.data_table= ft.DataTable(
            expand=True,
            border=ft.border.all(2, "purple"),
            #data_row_color= (ft.MaterialState.SELECTED, 
                #ft.MaterialState.PRESSED),
            border_radius=10,
            show_checkbox_column= True,
            columns=[
                ft.DataColumn(ft.Text("Id", color="purple",weight="bold")),
                ft.DataColumn(ft.Text("Nombre", color="purple",weight="bold")),
                ft.DataColumn(ft.Text("Edad", color="purple",weight="bold"), numeric=True),
                #ft.DataColumn(ft.Text("Acciones", color="purple",weight="bold")),
            ]
        )

        self.show_data()

        self.form= ft.Container(
            bgcolor="#222222",
            border_radius=10,
            col=4,
            padding=10,
            
            content=ft. Column(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                width=80,
                controls=[
                    ft.Text(
                        "Ingrese sus datos",
                        size=40,
                        text_align="center",
                        font_family="vivaldi",
                        color="white",
                    ),
                    self.name,
                    self.age,
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.TextButton(
                                    text="Guardar",
                                    icon=ft.icons.SAVE,
                                    style=ft.ButtonStyle(
                                        color="white",
                                        bgcolor="purple",
                                    ),
                                    on_click = self.add_data
                                ),
                                ft.TextButton(
                                    text="Actualizar",
                                    icon=ft.icons.UPDATE,
                                    style=ft.ButtonStyle(
                                        color="white",
                                        bgcolor="purple",
                                    )
                                ),
                                ft.TextButton(
                                    text="Borrar",
                                    icon=ft.icons.DELETE,
                                    style=ft.ButtonStyle(
                                        color="white",
                                        bgcolor="purple",
                                    )
                                ),
                            ]
                        )
                    )
                ]
            )
        )

        self.table= ft.Container(
            bgcolor="#222222",
            border_radius=10,
            col=8,
            content= ft.Column(
                controls=[
                    ft.Container(
                        padding=10,
                        content= ft.Row(
                            controls=[
                                self.search_filed,
                                ft.IconButton(
                                    tooltip="Editar",
                                    icon=ft.icons.EDIT,
                                    icon_color= "white"
                                ),
                                ft.IconButton(
                                    tooltip="Descargar en PDF",
                                    icon=ft.icons.PICTURE_AS_PDF,
                                    icon_color= "white"
                                ),
                                ft.IconButton(
                                    tooltip="Descargar en EXCEL",
                                    icon=ft.icons.SAVE_ALT,
                                    icon_color= "white"
                                )
                            ]
                        )
                    ),                    
                    ft.Column(
                        expand=True,
                        scroll="auto",
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

    #Metodo para mostrar los datos en la datatable
    def show_data(self):
        self.data_table.rows= []
        for x in self.data.get_users():
            self.data_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(x[0], color="white")),
                        ft.DataCell(ft.Text(x[1], color="white")),
                        ft.DataCell(ft.Text(str(x[2]), color="white"))
                    ]
                )
            )
        self.update()

    #Metodo para insertar datos a la tabla
    def add_data(self, e):
        name1 = self.name.value
        age1 = self.age.value
        try:
            if name1 != "" and age1 != "":
                user_exists = False
                for row in self.data.get_users():
                    if row[1] == name1:
                        user_exists = True
                        break
                if not user_exists:
                    self.clean_fileds()
                    self.data.add_users(name1, age1)
                    self.show_data()
        except ValueError as error:
            print(error)         

    def clean_fileds(self):
        self.name.value = ""
        self.age.value = ""

    def build(self):
        return self.conent

def main(page: ft.Page):
    page.bgcolor = "black"
    page.title=" CRUD MySQL"
    page.window.min_height =500
    page.window.min_width =100

    page.add(Form(page))


ft.app(main)
