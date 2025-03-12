import flet as ft


# Classe para criar tarefas
class Task(ft.Column):
    def __init__(self, task_name, task_status_change, task_delete):
        super().__init__()
        self.completed = False
        self.task_name = task_name
        self.task_status_change = task_status_change
        self.task_delete = task_delete

        self.display_task = ft.Checkbox(
            value=False,
            label=self.task_name.capitalize(),
            label_style=ft.TextStyle(weight="bold", size=20),
            on_change=self.status_change,
            check_color="#00FF00",
            fill_color="#000000"
        )

        self.edit_name = ft.TextField(
            expand=True,
            on_submit=self.save_clicked
        )

        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
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
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
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
        self.completed = self.display_task.value
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
            border_color="#97B4FF",
            filled=True,
            text_size=20,
        )

        # Lista de tarefas
        self.tasks = ft.Column(
            scroll=ft.ScrollMode.ALWAYS, height=450)

        # Filtros de tarefas
        self.filter = ft.Tabs(
            scrollable=False,
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[
                ft.Tab(text="Todas"),
                ft.Tab(text="Pendentes"),
                ft.Tab(text="Concluídas"),
            ]
        )

        # Contador de tarefas
        self.items_left = ft.Text(
            "0 tarefas adicionadas")

        self.button_clear = ft.OutlinedButton(
            text="Apagar tarefas concluídas",
            on_click=self.clear_completed_tasks,
            disabled=True,
        )

        # Adicionando elementos à interface
        self.controls = [
            # Inserção de tarefas
            ft.Row(
                controls=[
                    self.new_task,
                    ft.FloatingActionButton(
                        icon=ft.Icons.ADD,
                        on_click=self.add_task,
                        tooltip="Adicionar tarefa",
                        bgcolor="purple",),

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
                            self.button_clear,
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
            if task.completed:
                self.task_delete(task)

    def task_status_change(self, task):
        self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()

    def before_update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        count = 0
        task_complete = 0
        for task in self.tasks.controls:
            task.visible = (
                status == "Todas" or (status == "Pendentes" and task.completed == False) or (
                    status == "Concluídas" and task.completed == True)
            )

            if not task.completed:
                count += 1

            if task.completed:
                task_complete += 1

        if task_complete > 0:
            self.button_clear.disabled = False
        else:
            self.button_clear.disabled = True

        self.items_left.value = f"{count} Tarefa(s) não concluída(s)"
        super().before_update()


def main(page: ft.Page):
    page.title = "Minhas Tarefas"
    page.window.width = 600
    page.window.height = 750
    # Desligo a opção de maximizar
    page.window.maximizable = False
    # Não posso mais mudar o tamanho da janela do app
    page.window.resizable = False
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    def theme_change(e):
        page.theme_mode = (
            ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        )

        theme_icon.icon = (
            ft.Icons.WB_SUNNY_OUTLINED if page.theme_mode == ft.ThemeMode.LIGHT else ft.Icons.DARK_MODE_OUTLINED
        )

        page.update()

    page.theme_mode = ft.ThemeMode.LIGHT

    theme_icon = ft.IconButton(
        icon=ft.Icons.WB_SUNNY_OUTLINED,
        tooltip="Alternar tema",
        on_click=theme_change
    )

    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Column(
                    alignment=ft.MainAxisAlignment.START,
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Text(value="Minhas Tarefas", size=44,
                                        weight="bold", color="purple")
                            ]
                        )
                    ]
                ),
                ft.Column(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[
                        theme_icon
                    ]
                )
            ]
        )
    )
    page.update()

    # Criando a aplicação
    app = TodoApp()

    # Adicionando a aplicação à página
    page.add(app)


ft.app(target=main)
