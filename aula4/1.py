import flet as ft


def main(page: ft.Page):
    def add_task(e):
        print(new_task)
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        page.update()

    new_task = ft.TextField(hint_text="Adicione uma tarefa ...", expand=True)
    new_button = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_task)

    cards = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    new_task, new_button
                ]
            )
        ]
    )

    page.add(cards)

    # Nessa aula parendemos que ao invés de ficar adicionando um por um componente no page.add
    # O correto é criar um coponente que possui uma coluna e nessa coluna colocar todas
    # as variáveis que desejamos adicionar na página.


ft.app(target=main)
