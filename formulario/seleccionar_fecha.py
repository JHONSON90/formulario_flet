import datetime
import flet as ft



def seleccionar_fecha():
    class Fecha_seleccionada(ft.Column):
        def __init__(self):
            super().__init__()
            self.datepicker = ft.DatePicker(
                first_date=datetime.datetime(2022, 10, 1),
                last_date=datetime.datetime(2026, 10, 1),
                on_change=self.change_date,
            )

            self.selected_date = ft.Text()

            self.controls = [
                ft.ElevatedButton(
                    "Pick date",
                    color="#858796",
                    bgcolor="#858796",
                    icon=ft.icons.CALENDAR_MONTH,
                    icon_color="#858796",
                    on_click=self.open_date_picker,
                    
                    
                ),
                self.selected_date,
            ]

        def open_date_picker(self, e):
            # self.datepicker.pick_date()
            e.control.page.open(self.datepicker)

        def change_date(self, e):
            self.selected_date.value = f"Fecha seleccionada: {self.datepicker.value}"
            e.control.page.update()

        # happens when example is added to the page (when user chooses the DatePicker control from the grid)
        def did_mount(self):
            self.page.overlay.append(self.datepicker)
            self.page.update()

        # happens when example is removed from the page (when user chooses different control group on the navigation rail)
        def will_unmount(self):
            self.page.overlay.remove(self.datepicker)
            self.page.update()

    fechas_seleccionada = Fecha_seleccionada()

    return fechas_seleccionada