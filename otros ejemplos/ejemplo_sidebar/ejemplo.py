import flet as ft 

class SideBar(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        
        page.title = "sidebar"
        # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.auto_scroll = True
        page.scroll = ft.ScrollMode.AUTO

        
        self.drawer = ft.Column(
            width= 100,
            #bgcolor = "red",
            height= 400,
            alignment = ft.MainAxisAlignment.START,
            expand = True,
            controls = [
                ft.Container(height=12),
                ft.IconButton(
                    #label =  "Home",
                    icon = ft.icons.HOME,
                    hover_color= ft.colors.BLUE_GREY_50,
                    #selected_icon_content = ft.icons.HOME_ROUNDED,
                    on_click= lambda _: page.go("/home")
                ), 
                #ft.Divider(thickness=1,  color="gray"),

                ft.IconButton(
                    icon=ft.icons.MAIL,
                    hover_color= ft.colors.BLUE_GREY_50,

                #label="Item 2",
                #selected_icon=ft.icons.MAIL,
                    on_click= lambda _: page.go("/mail")
                ),
            ],
        )
    
        
        
        
    # def handle_dimissal(self, e):
    #     self.page.add(ft.Text("home"))
        
    # def handle_change(self, e):
    #     self.page.add(ft.Text(f"index cambiado: {e.selected_index}"))
        
    def build(self):
        return ft.Container(
            width=50,
            height=640,
            bgcolor = "transparent",
            border=ft.border.all(color="red"),
            content=self.drawer
        )
    
    

        
        
def main(page: ft.Page):
    page.bgcolor = "white"
    page.title=" CRUD MySQL"
    page.window.min_height =500
    page.window.width = 80
    app = SideBar(page)
    page.add(app.build())



ft.app(main)