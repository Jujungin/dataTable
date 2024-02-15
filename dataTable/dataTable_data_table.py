import flet as ft
from dataTable_controls import add_to_control_reference

class AppDataTable(ft.UserControl):
    def __init__(self):
        super().__init__()

    def app_data_table_instance(self):
        add_to_control_reference("AppDataTable", self)

    def build(self):
        self.app_data_table_instance()
        return ft.Row(
            expand=True,
            controls=[
                ft.DataTable(
                    expand=True,
                    border=ft.border.all(2, "#ebebeb"),
                    border_radius=8,
                    horizontal_lines=ft.border.BorderSide(1, "#ebebeb"),
                    columns=[
                        ft.DataColumn(
                            ft.Text(
                                "Column 1", 
                                size=12, 
                                color="black",
                                weight="bold",
                            ),
                        ),
                        ft.DataColumn(
                            ft.Text(
                                "Column 2", 
                                size=12, 
                                color="black",
                                weight="bold",
                            ),
                        ),
                        ft.DataColumn(
                            ft.Text(
                                "Column 3", 
                                size=12, 
                                color="black",
                                weight="bold",
                            ),
                        ),
                        ft.DataColumn(
                            ft.Text(
                                "Column 4", 
                                size=12, 
                                color="black",
                                weight="bold",
                            ),
                        ),
                    ],
                    rows=[

                    ],          
                )
            ],
        )
    