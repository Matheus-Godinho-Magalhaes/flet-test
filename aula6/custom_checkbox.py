import flet as ft


class Checkbox(ft.Row):
    def __init__(self, text):
        super().__init__()
        self.text_view = ft.Text(text)
        self.text_edit = ft.TextField(value=text, visible=False)
        self.edit_button = ft.IconButton(
            icon=ft.Icons.EDIT, on_click=self.edit)
        self.save_button = ft.IconButton(icon=ft.Icons.SAVE, on_click=self.save,
                                         visible=False)
        self.delete_button = ft.IconButton(
            icon=ft.Icons.DELETE, on_click=self.delete)

        self.controls = [
            ft.Checkbox(),
            self.text_view,
            self.text_edit,
            self.edit_button,
            self.save_button,
            self.delete_button,
        ]

    def edit(self, e):
        pass

    def save(self, e):
        pass

    def delete(self, e):
        pass
