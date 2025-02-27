import flet as ft


def main(page: ft.Page):

    def add_task(e):
        # Toda vez que eu criar uma função eu tenho que passar o parâmetro e que significa event
        # que seria o evento desse botão
        print(new_task.value)

    new_task = ft.TextField(hint_text="Insira uma tarefa: ... ")

    new_button = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_task)
    # Para colocar uma ação nesse botão, basta eu acessar o atributo on_click
    # e fornecer uma função para ele

    page.add(new_task, new_button)

    # Ao final dessa aula aprendemos a criar variáveis, a dar função uma ação ao nosso botão
    # e mostrar o valor desse on_click


ft.app(target=main)
