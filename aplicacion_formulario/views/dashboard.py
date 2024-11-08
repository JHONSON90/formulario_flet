import flet as ft
import locale
from data.peticiones import UserManager

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

    # REGION: Dashboard
class Dashboard(ft.UserControl):
    def __init__(self, page):
        super().__init__(expand=True)
        self.page = page
        self.data = UserManager()
        self.alignment = ft.alignment.center
        
        valor1 = self.valor_total()
        valor2 = self.valor_cobrado()

#Region: Tarjetas
        self.tarjeta_con_total = ft.Card(
            content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.ListTile(
                                subtitle = ft.Text("Valor Total Recibido"),
                                title = ft.Text(
                                    locale.currency(valor1, grouping=True),
                                                size=48,
                                                weight="bold"
                                                )
                                )
                            ]               
                        ),
                    width = 490,
                    padding=10
                    ),                            
                )
        
        self.tarjeta_con_total_Recaudado = ft.Card(
            content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.ListTile(
                                subtitle = ft.Text("Valor Total Cobrado"),
                                title = ft.Text(
                                    locale.currency(valor2, grouping=True),
                                                size=48,
                                                weight="bold"
                                                ),
                                )
                            ]               
                        ),
                    width = 490,
                    padding=10
                    ),                            
                )
    
        self.seguimiento_mensual = ft.LineChart(
                    data_series=[
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(1, 2),
                    ft.LineChartDataPoint(3, 1.5),
                    ft.LineChartDataPoint(5, 1.4),
                    ft.LineChartDataPoint(7, 3.4),
                    ft.LineChartDataPoint(10, 2),
                    ft.LineChartDataPoint(12, 2.2),
                    
                ],
                stroke_width=8,
                color=ft.colors.LIGHT_GREEN,
                curved=True,
                stroke_cap_round=True,
            ),
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(1, 1),
                    ft.LineChartDataPoint(3, 2.8),
                    ft.LineChartDataPoint(5, 1.2),
                    ft.LineChartDataPoint(7, 2.8),
                    ft.LineChartDataPoint(10, 2.6),
                    ft.LineChartDataPoint(12, 3.9),
                ],
                color=ft.colors.PINK,
                below_line_bgcolor=ft.colors.with_opacity(0, ft.colors.PINK),
                stroke_width=8,
                curved=True,
                stroke_cap_round=True,
            ),
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(1, 2.8),
                    ft.LineChartDataPoint(3, 1.9),
                    ft.LineChartDataPoint(5, 3),
                    ft.LineChartDataPoint(7, 1.3),
                    ft.LineChartDataPoint(10, 2.6),
                    ft.LineChartDataPoint(12, 2.5),
                ],
                color=ft.colors.CYAN,
                stroke_width=8,
                curved=True,
                stroke_cap_round=True,
            ),
        ],
                    border=ft.Border(
                        bottom=ft.BorderSide(4, ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE))
                    ),
                    left_axis=ft.ChartAxis(
                        labels=[
                            ft.ChartAxisLabel(
                                value=1,
                                label=ft.Text("1m", size=14, weight=ft.FontWeight.BOLD),
                            ),
                            ft.ChartAxisLabel(
                                value=2,
                                label=ft.Text("2m", size=14, weight=ft.FontWeight.BOLD),
                            ),
                            ft.ChartAxisLabel(
                                value=3,
                                label=ft.Text("3m", size=14, weight=ft.FontWeight.BOLD),
                            ),
                            ft.ChartAxisLabel(
                                value=4,
                                label=ft.Text("4m", size=14, weight=ft.FontWeight.BOLD),
                            ),
                            ft.ChartAxisLabel(
                                value=5,
                                label=ft.Text("5m", size=14, weight=ft.FontWeight.BOLD),
                            ),
                            ft.ChartAxisLabel(
                                value=6,
                                label=ft.Text("6m", size=14, weight=ft.FontWeight.BOLD),
                            ),
                        ],
                        labels_size=40,
                    ),
                    bottom_axis=ft.ChartAxis(
                        labels=[
                            ft.ChartAxisLabel(
                                value=2,
                                label=ft.Container(
                                    ft.Text(
                                        "SEP",
                                        size=16,
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                                    ),
                                    margin=ft.margin.only(top=10),
                                ),
                            ),
                            ft.ChartAxisLabel(
                                value=7,
                                label=ft.Container(
                                    ft.Text(
                                        "OCT",
                                        size=16,
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                                    ),
                                    margin=ft.margin.only(top=10),
                                ),
                            ),
                            ft.ChartAxisLabel(
                                value=12,
                                label=ft.Container(
                                    ft.Text(
                                        "DEC",
                                        size=16,
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                                    ),
                                    margin=ft.margin.only(top=10),
                                ),
                            ),
                        ],
                        labels_size=32,
                    ),
                    tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLUE_GREY),
                    min_y=0,
                    max_y=4,
                    min_x=0,
                    max_x=14,
                    # animate=5000,
                    expand=True,
                )
                
        self.mayores_clientes = ft.PieChart(
                    sections=[
                        self.tipos_de_servicio()
                        ],
                    sections_space=0,
                    center_space_radius=40,
                    expand=True
                )
        
        self.content = ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        self.tarjeta_con_total,
                                        self.tarjeta_con_total_Recaudado,
                                    ]
                                ),
                                self.mayores_clientes,
                                self.seguimiento_mensual
                            ]
                        )
                    )
    
    def valor_total(self):
        valor = self.data.total_recibido()
        return valor[0] * 1
        
    def valor_cobrado(self):
        valor2 = self.data.total_cobrado()
        return valor2[0]*1
        
    def consolidado_mensual_recibido(self):
        self.data.total_recibido_mensual()
        
    def consolidado_mensual_cobrado(self):
        self.data.total_cobrado_mensual()
        
    def tipos_de_servicio(self):
        datossections = []
        colors= ["RED", "PURPLE", "GREEN", "BLUE", "YELLOW", "INDIGO"]
        for i, resultado in self.data.total_recibido_tipos():
            tipo = resultado[0]
            valor = resultado[1]
            datossections.append(
                ft.PieChartSection(valor, title=tipo, color=colors[i], radius= 50)
            )
        
        
    def build(self):
        return self.content

# def main(page):
    
#     dash = Dashboard(page)
#     page.add(dash),
    
# ft.app(main)
