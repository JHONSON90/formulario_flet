import flet as ft 


class Menu_expansible(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        self.alignment = ft.alignment.center
        self.panel = self._create_panel(page)

    def _create_panel(self, page: ft.Page) -> ft.ExpansionPanelList:
        panels = [
            self._create_expansion_panel("Peticiones", "Son solicitudes formales que se hacen a una entidad para que realice alguna acción o gestione un trámite", lambda _: page.go("/formulario_pqrs")),
            self._create_expansion_panel("Quejas", "Expresan el descontento de una persona frente a un servicio o producto que no cumple con lo esperado.", lambda _: page.go("/formulario_pqrs")),
            self._create_expansion_panel("Reclamos", "Son solicitudes formales para que se corrija una situación que causa un perjuicio o daño.", lambda _: page.go("/formulario_pqrs")),
            self._create_expansion_panel("Sugerencias", "Son propuestas para mejorar un servicio o producto.", lambda _: page.go("/formulario_pqrs")),
        ]

        return ft.ExpansionPanelList(
            elevation=8,
            divider_color=ft.colors.AMBER,
            on_change=self.handle_change,
            controls=panels
        )

    def _create_expansion_panel(self, title: str, body: str, on_click: callable) -> ft.ExpansionPanel:
        return ft.ExpansionPanel(
            header=ft.ListTile(title=ft.Text(title)),
            content=ft.Container(
                content=ft.Column([
                    ft.Text(body, width=300),
                    ft.ElevatedButton("Ir a formulario", on_click=on_click)
                ]),
                padding=ft.Padding(5, 0, 5, 5)
            )
        )
    def handle_change(self, e: ft.ControlEvent):
        print(f"cambio del panel con index {e.data}")

    def build(self):
        return self.panel
        
