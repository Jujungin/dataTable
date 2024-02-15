import flet as ft
from dataTable_controls import add_to_control_reference
from dataTable_btn import return_form_button

class AppForm(ft.UserControl):
    def __init__(self):
        super().__init__()

    def app_form_input_instance(self):
        add_to_control_reference("AppForm", self)

    def app_form_input_field(self, name:str, expand:int):
        return ft.Container(
            expand=expand,
            height=45,
            bgcolor="#ebebeb",
            border_radius=6,
            padding=8,
            content=ft.Column(
                spacing=1,
                controls=[
                    ft.Text(
                        value=name, 
                        size=9, 
                        color="black", 
                        weight="bold",
                    ),
                    ft.TextField(
                        border_color="transparent",
                        height=20,
                        text_size=13,
                        content_padding=0,
                        cursor_color="black",
                        cursor_width=1,
                        cursor_height=18,
                        color="black",
                    )
                ],
            )
        )


    def build(self):
        self.app_form_input_instance()
        return ft.Container(
            expand=True,
            height=190,
            bgcolor="white10",
            border=ft.border.all(1, "#ebebeb"),
            border_radius=8,
            padding=15,
            content=ft.Column(
                expand=True,
                controls=[
                    ft.Row(
                        controls=[
                            self.app_form_input_field("Field *", True)
                        ],
                    ),
                    ft.Row(
                        controls=[
                            self.app_form_input_field("Field 1 *", 3),
                            self.app_form_input_field("Field 2 *", 1),
                            self.app_form_input_field("Field 3 *", 1),
                        ],
                    ),
                    ft.Divider(
                        height=1,
                        color="transparent",
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            return_form_button(),
                        ]
                    )
                ],
            )
        )