import flet as ft
from custom_checkbox import Checkbox


def main(page: ft.Page):

    page.title = "Minhas tarefas"

    page.window.width = 400
    page.window.height = 650

    page.theme_mode = ft.ThemeMode.LIGHT

    page.padding = ft.padding.only(left=20, right=20, top=20, bottom=20)

    def add_task(e):
        print(new_task.value)
        task_list.controls.append(Checkbox(new_task.value))
        new_task.value = ""
        page.update()
        # Colocando o campo em foco
        new_task.focus()

    new_task = ft.TextField(
        hint_text="Adicione uma tarefa ...", expand=True, autofocus=True)
    new_button = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_task)

    task_list = ft.Column()

    cards = ft.Column(
        width=400,
        controls=[
            ft.Row(
                controls=[
                    new_task, new_button
                ]
            ),
            task_list
        ]
    )

    page.add(cards)

    # Nessa aula aprendemos a colocar autofoco, a usar os botoes.


ft.app(target=main)
