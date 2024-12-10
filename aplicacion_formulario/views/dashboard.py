import flet as ft
from flet.plotly_chart import PlotlyChart
import locale
import plotly.graph_objects as go

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
        page.scroll = "always"
        page.bgcolor = ft.colors.INDIGO_50
        self.data = UserManager()
        self.alignment = ft.alignment.center
        
    
        
        valor1 = self.valor_total()
        valor2 = self.valor_cobrado()
        fig = self.consolidado_mensual_recibido()
        fig2 = self.total_por_tipo()
        maximos = self.maximo()
        maximos_cobrados = self.get_maximo_cobrado()
        

#Region: Tarjetas
        self.tarjeta_con_total = ft.Card(
            color="#bdcbf4",   #858796",
            content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.ListTile(
                                subtitle = ft.Text("Valor Total Recibido",color='#4e73df',),
                                title = ft.Text(
                                  locale.currency(valor1, grouping=True),
                                                size=48,
                                                weight="bold",
                                                color='white',
                                                )
                                )
                            ]               
                        ),
                    width = 490,
                    padding=10
                    ),                            
                )
        
        self.tarjeta_con_total_Recaudado = ft.Card(
            color="#bdcbf4",   #858796",
            content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.ListTile(
                                subtitle = ft.Text("Valor Total Cobrado",color='#4e73df',),
                                title = ft.Text(
                                  locale.currency(valor2, grouping=True),
                                                size=48,
                                                weight="bold",
                                                color='white',
                                                ),
                                )
                            ]               
                        ),
                    width = 400,
                    padding=10
                    ),                            
                )
        
        self.tarjeta_maximo_recibido = ft.Card(
            color="#bdcbf4",   #858796",
            content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.ListTile(
                                subtitle = ft.Text("Valor maximo recibido por consignación",color='#4e73df',),
                                title = ft.Text(
                                  locale.currency(maximos, grouping=True),
                                                size=48,
                                                weight="bold",
                                                color='white',
                                                ),
                                )
                            ]               
                        ),
                    width = 350,
                    padding=10
                    ),                            
                )
        
        self.tarjeta_con_maximo_cobrado = ft.Card(
            color="#bdcbf4",   #858796",
            content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.ListTile(
                                subtitle = ft.Text("Maximo Cobrado a un cliente",color='#4e73df',),
                                title = ft.Text(
                                  locale.currency(maximos_cobrados, grouping=True),
                                                size=48,
                                                weight="bold",
                                                color='white',
                                                ),
                                )
                            ]               
                        ),
                    width = 350,
                    padding=10
                    ),                            
                )
    
        self.seguimiento_mensual = ft.Container(
            width = "750",
            height="450",
            content= PlotlyChart(fig, 
                                 expand = True)
        )
                
        self.tipo_de_servicio = ft.Container(
            width = "750",
            height= "450",
            content= PlotlyChart(fig2,
                                 expand=True)
        )
    
        self.content = ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    
                                    wrap=True,
                                    spacing=10,
                                    run_spacing=10,
                                    controls=[
                                        self.tarjeta_con_total,
                                        self.tarjeta_con_total_Recaudado,
                                        self.tarjeta_con_maximo_cobrado,
                                        self.tarjeta_maximo_recibido
                                    ]
                                ),
                                ft.Row(
                                    wrap=True,
                                    spacing=5,
                                    run_spacing=5,
                                    controls=[
                                        self.seguimiento_mensual,
                                        self.tipo_de_servicio
                                    ]
                                )
                                
                    
                            ]
                        )
                    )
    
    def valor_total(self):
        valor = self.data.total_recibido()
        return valor[0] * 1
        
    def valor_cobrado(self):
        valor2 = self.data.total_cobrado()
        return valor2[0]*1
    
    def maximo(self):
        valor = self.data.maximo_recibido()
        return valor[0] * 1
    
    def minimo(self):
        valor = self.data.minimo_recibido()
        return valor[0] * 1
    
    def get_maximo_cobrado(self):
        valor = self.data.maximo_cobrado()
        return valor[0] * 1
    
    def get_minimo_cobrado(self):
        valor = self.data.minimo_cobrado()
        return valor[0] * 1
        
    def consolidado_mensual_recibido(self):
            
            minimos = self.minimo()
            maximos = self.maximo()
            minimos_cobrados = self.get_minimo_cobrado()
            maximos_cobrados = self.get_maximo_cobrado()
            fig = go.Figure()
            
            for row in self.data.total_recibido_mensual():
                fig.add_trace(
                    go.Bar(
                        x=[int(row[0])], 
                        y=[int(row[1])],
                        name= "Seguimiento Mensual",
                        marker=dict(color='paleturquoise'),
                        )
                )
            
            for row in self.data.total_cobrado_mensual():
                fig.add_trace(
                    go.Scatter(
                            x=[int(row[0])],
                            y=[int(row[1])],
                            yaxis="y2",
                            mode="lines+markers",
                            name="Total Cobrado",
                            marker=dict(color='crimson'),
                            line=dict(color='crimson')
                            
                    )
                )
            
            fig.update_layout(
                legend= dict(orientation="h"),
                # width=650,
                # height=450,
                xaxis=dict(
                    tickmode="linear",
                    dtick=1,  # Mostrar solo valores enteros
                    title="Mes"
                ),
                yaxis=dict(
                    title=dict(text="Total Recibido"),
                    side="left",
                    range=[minimos, maximos], 
                ),
                yaxis2=dict(
                    title=dict(text="Total cobrado a clientes"),
                    side="right",
                    range=[minimos_cobrados,maximos_cobrados], 
                    overlaying="y",
                    tickmode="sync",
                ),
            )
            return fig
        
    def total_por_tipo(self):
        fig = go.Figure()
        for row in self.data.total_recibido_tipos():
            fig.add_trace(
                go.Bar(
                    x=[row[0]],
                    y=[int(row[1])],
                    name="Tipo de Servicio",
                )
            )
        
        fig.update_layout(
            legend= dict(orientation="h"),
            #autosize=True,
            # minreducedwidth=250,
            # minreducedheight=250,
            #width=650,
            #height=450,
        # yaxis=dict(
        #     title=dict(
        #         text="Y-axis Title",
        #         font=dict(
        #             size=30
        #         )
        #     ),
        #     ticktext=[row[0]],
        #     tickvals=[int(row[1])],
        #     tickmode="array",
        # )
    )
        return fig
       
        
    def build(self):
        return self.content

# def main(page):
    
#     dash = Dashboard(page)
#     page.add(dash),
    
# ft.app(main)
