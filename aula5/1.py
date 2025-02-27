import flet as ft


def main(page: ft.Page):

    # Adicionando um título para a minha aplicação
    page.title = "Minhas tarefas"

    # Configurando as dimensões iniciais do meu apicativo quando for aberto pela 1 vez
    page.window.width = 400
    page.window.height = 650

    # Mudando o tema da aplicação
    page.theme_mode = ft.ThemeMode.LIGHT

    # Configurando as "margens" da minha aplicação para não ficar muito colado na borda
    page.padding = ft.padding.only(left=20, right=20, top=20, bottom=20)

    def add_task(e):
        print(new_task.value)

        # Agora eu estou adicionando cada um dos inputs dos valores de
        # new_task dentro da variável task_list.
        task_list.controls.append(ft.Checkbox(label=new_task.value))

        new_task.value = ""
        page.update()

    new_task = ft.TextField(hint_text="Adicione uma tarefa ...", expand=True)
    new_button = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_task)

    task_list = ft.Column()

    cards = ft.Column(
        # Configurando o comprimento da linha
        width=400,
        controls=[
            ft.Row(
                controls=[
                    new_task, new_button
                ]
            ),
            # Logo depois eu estarei mostrando a task_list com todos os
            # seus valores guardados.
            task_list
        ]
    )

    page.add(cards)

    # Nessa aula aprendemosa adicionar um título, configurar o tamanho de início da aplicação,
    # mudar o tema, configurar as bordas, armazenar os valores em uma variável ft.Column.


ft.app(target=main)
