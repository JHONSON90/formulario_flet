import flet as ft 

# configuracion del main

def main(page: ft.Page):
    page.title = "contador de prueba"
    page.vertical_alignment= ft.MainAxisAlignment.CENTER # alineamos la pagina al centro
    
    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    
    def disminuir(e):
        txt_number.value =  str(int(txt_number.value)-1)   
        page.update()
    
    def aumentar(e):
        txt_number.value = str(int(txt_number.value)+1)
        page.update()
    
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click = disminuir),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click = aumentar),
            ],
            alignment = ft.MainAxisAlignment.CENTER
        )
    )
ft.app(main)
