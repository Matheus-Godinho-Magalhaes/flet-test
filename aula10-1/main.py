import flet as ft


# Classe para criar as tarefas
class Task(ft.Column):
    pass


# Classe para criar o aplicativo
class TodoApp(ft.Column):
    def build(self):
        self.new_task = ft.TextField(
            hint_text="Qual tarefa precisa ser feita?",
            expand=True,
            on_submit=self.add_task,
        )

        self.tasks = ft.Column()

        self.filter = ft. Tabs(
            scrollable=False,
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[
                ft.Tab(text="Todas"),
                ft.Tab(text="Ativas"),
                ft.Tab(text="Concluídas"),
            ]
        )

        self.items_left = ft.Text("0 tarefas adicionas")

        return ft.Column(
            controls=[
                # Título da aplicação
                ft.Row(
                    controls=[
                        ft.Text(value="Tarefas")
                    ]
                ),
                ft.Row(),
                ft.Column()
            ]
        )

    def add_task(self, e):
        pass

    def tabs_changed(self, e):
        pass


def main(page: ft.Page):
    page.title = "Minhas Tarefas"
    page.window.width = 600
    page.window.height = 650
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = ft.padding.only(left=20, top=20, right=20, bottom=20)
    page.theme_mode = ft.ThemeMode.LIGHT
    page.update()

    app = TodoApp()

    page.add(app)


ft.app(target=main)
