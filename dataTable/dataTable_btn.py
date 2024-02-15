import flet as ft
from dataTable_controls import return_control_reference
from dataTable_form_helper import FormHelper

control_map = return_control_reference()

def update_text(e):
    e.control.content.controls[0].read_only = False
    e.control.content.controls[0].update()

def get_input_data(e):
    for key, value in control_map.items():
        if key == "AppForm":
            data = ft.DataRow(
                cells=[]
            )
            for user_input in value.controls[0].content.controls[0].controls[:]:
                data.cells.append(
                    ft.DataCell(
                        FormHelper(user_input.content.controls[1].value),
                        on_double_tap=lambda e: update_text(e),
                    )
                )
                # print(user_input.content.controls[1].value)
            for user_input in value.controls[0].content.controls[1].controls[:]:
                data.cells.append(
                    ft.DataCell(
                        FormHelper(user_input.content.controls[1].value),
                        on_double_tap=lambda e: update_text(e),
                    )
                )
                # print(user_input.content.controls[1].value)
        if key == "AppDataTable":
            value.controls[0].controls[0].rows.append(data)
            value.controls[0].controls[0].update()


def return_form_button():
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.ElevatedButton(
            on_click=lambda e: get_input_data(e),
            bgcolor="#081d33",
            color="white",
            content=ft.Row(
                controls=[
                    ft.Icon(
                        name=ft.icons.ADD_ROUNDED,
                        size=12,
                    ),
                    ft.Text(
                        "Add Input Field To Table",
                        size=11,
                        weight="bold",
                    )
                ],
            ),
            style=ft.ButtonStyle(
                shape={
                    "": ft.RoundedRectangleBorder(
                        radius=6,
                    )
                },
                color={
                    "": "white",
                }
            ),
            height=42,
            width=220,
        ),
    )