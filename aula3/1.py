import flet as ft


def main(page: ft.Page):
    def add_task(e):
        print(new_task)
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        page.update()

    new_task = ft.TextField(hint_text="Adicione uma tarefa ...")
    new_button = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_task)

    page.add(new_task, new_button)


    # Nessa aula aprendemos a como adicionar outro tipo de classe (checkbox) e que
    # devemos recarregar a página para poder ver as atualizações
ft.app(target=main)
