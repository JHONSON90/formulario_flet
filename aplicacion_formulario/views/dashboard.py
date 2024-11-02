import flet as ft
import locale


locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

base_chart_style: dict ={
    "expand": True,
    "tooltip_bgcolor": ft.colors.with_opacity(0.8, ft.colors.AMBER),
    "left_axis": ft.ChartAxis(labels_size=50),
    "bottom_axis":ft.ChartAxis(labels_interval=1, labels_size=40),
    "horizontal_grid_lines": ft.ChartGridLines(
        interval=10,
        color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE),width=1
    ),

}

def main(page):
    page.add(
            # ft.Card(
            #     content=ft.Container(
            #         content=ft.Column(
            #             controls=[
            #                 ft.ListTile(
            #                     subtitle = ft.Text("Valor Total Recibido"),
            #                     title = ft.Text(locale.currency(2000000000, grouping=True),
            #                                     size=48,
            #                                     weight="bold"
            #                                     ),#TODO: colocar el valor traido por base de datos'''
            #                     )
            #                 ]               
            #             ),
            #         width = 490,
            #         padding=10
            #         ),                            
            #     ),
            
            ft.PieChart(
                sections=[
                    ft.PieChartSection(40, 
                                       title="40%", 
                                       color=ft.colors.AMBER,
                                       radius=50
                                       ),
                    ft.PieChartSection(30, 
                                       title="30%", 
                                       color=ft.colors.BLUE,
                                       radius=50
                                       ),
                    ft.PieChartSection(15, 
                                       title="15%", 
                                       color=ft.colors.GREEN,
                                       radius=50
                                       ),
                    ft.PieChartSection(15, 
                                       title="15%", 
                                       color=ft.colors.RED,
                                       radius=50
                                       ),
                ],
                sections_space=0,
                center_space_radius=40,
                expand=True
            ),
            ft.Rive(
                src="https://rive.app/community/files/12338-23750-hasty-driver/",
                placeholder=ft.ProgressBar(),
                width=490,
                height=490
            )
            
            ),
    
ft.app(main)
