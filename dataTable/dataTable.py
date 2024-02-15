import flet as ft
from dataTable_header import AppHeader
from dataTable_form import AppForm
from dataTable_data_table import AppDataTable

def main(page: ft.Page):
    page.bgcolor = "#fdfdfd"
    page.padding = 20
    page.add(
        ft.Column(
          expand=True,
          controls=[
              AppHeader(),
              ft.Divider(
                height=2,
                color="transparent",
              ),
              AppForm(),
              ft.Column(
                scroll='hidden',
                expand=True,
                controls=[
                    AppDataTable(),
                ],
              ),
          ],
        ),
    )
    page.update()

if __name__ == "__main__":
    ft.app(target=main)