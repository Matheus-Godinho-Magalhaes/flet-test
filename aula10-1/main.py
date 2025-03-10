import flet as ft

# Classe para criar tarefas


class Task(ft.Column):
    def __init__(self, task_name, task_status_change, task_delete):
        super().__init__()
        self.complete = False
        self.task_name = task_name
        self.task_status_change = task_status_change
        self.task_delete = task_delete

        self.display_task = ft.Checkbox(
            value=False,
            label=self.task_name,
            on_change=self.status_change,
        )

        self.edit_name = ft.TextField(
            expand=True,
            on_submit=self.save_clicked
        )

        self.display_view = ft.Row(
            controls=[
                self.display_task,
                ft.Row(
                    controls=[
                        ft.IconButton(icon=ft.Icons.CREATE_OUTLINED,
                                      tooltip="Editar Tarefa",
                                      on_click=self.edit_clicked,
                                      icon_color=ft.Colors.GREEN),
                        ft.IconButton(icon=ft.Icons.DELETE_OUTLINED,
                                      tooltip="Deletar Tarefa",
                                      on_click=self.delete_clicked,
                                      icon_color=ft.Colors.RED)

                    ]
                )
            ]
        )

        self.edit_view = ft.Row(
            visible=False,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.Icons.DONE_OUTLINED,
                    tooltip="Atualizar tarefa",
                    on_click=self.save_clicked,
                    icon_color=ft.Colors.GREEN
                )
            ]
        )

        # Adicionando os controles diretamente ao Column
        self.controls = [self.display_view, self.edit_view]

    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.edit_view.visible = True
        self.edit_name.focus()
        self.display_view.visible = False
        self.update()

    def delete_clicked(self, e):
        self.task_delete(self)

    def status_change(self, e):
        self.complete = self.display_task.value
        self.task_status_change(self)


# Classe para criar o aplicativo


class TodoApp(ft.Column):
    def __init__(self):
        # Herdando da classe pai ft.Cloumn
        super().__init__()

        # Campo de entrada para novas tarefas
        self.new_task = ft.TextField(
            hint_text="Qual tarefa precisa ser feita?",
            expand=True,
            on_submit=self.add_task,
        )

        # Lista de tarefas
        self.tasks = ft.Column()

        # Filtros de tarefas
        self.filter = ft.Tabs(
            scrollable=False,
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[
                ft.Tab(text="Todas"),
                ft.Tab(text="Ativas"),
                ft.Tab(text="Concluídas"),
            ]
        )

        # Contador de tarefas
        self.items_left = ft.Text("0 tarefas adicionadas")

        # Adicionando elementos à interface
        self.controls = [
            # Título da aplicação
            ft.Row(
                controls=[
                    ft.Text(
                        value="Tarefas",
                        size=50,
                        weight="bold",
                        color=ft.Colors.with_opacity(0.9, "black")
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            # Inserção de tarefas
            ft.Row(
                controls=[
                    self.new_task,
                    ft.FloatingActionButton(
                        icon=ft.Icons.ADD, on_click=self.add_task),

                ]
            ),
            # Listagem de Tarefas
            ft.Column(
                controls=[
                    self.filter,
                    self.tasks,
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            self.items_left,
                            ft.OutlinedButton(
                                text="Apagar tarefas concluídas",
                                on_click=self.clear_completed_tasks,
                            )
                        ]
                    )
                ]
            )

        ]

    def add_task(self, e):
        if self.new_task.value:
            task = Task(self.new_task.value,
                        self.task_status_change, self.task_delete)
            self.tasks.controls.append(task)
            self.new_task.value = ""
            self.new_task.focus()
            self.update()

    def tabs_changed(self, e):
        self.update()

    def clear_completed_tasks(self, e):
        for task in self.tasks.controls[:]:
            if task.complete:
                self.task_delete(task)

    def task_status_change(self, task):
        self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()


def main(page: ft.Page):
    page.title = "Minhas Tarefas"
    page.window_width = 600
    page.window_height = 650
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT
    page.update()

    # Criando a aplicação
    app = TodoApp()

    # Adicionando a aplicação à página
    page.add(app)


ft.app(target=main)
