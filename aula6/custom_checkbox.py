import flet as ft  # Importa o framework Flet para criar interfaces gráficas.


# Define a classe Checkbox, que herda de ft.Row (uma linha de widgets).
class Checkbox(ft.Row):
    # Método construtor da classe. Recebe um parâmetro `text`.
    def __init__(self, text):
        # Chama o construtor da classe pai (ft.Row) para inicializar a linha.
        super().__init__()

        # Cria um widget de texto (ft.Text) para exibir o rótulo do checkbox.
        self.text_view = ft.Text(text)

        # Cria um campo de edição de texto (ft.TextField) com o valor inicial igual ao `text`.
        # Esse campo é inicialmente invisível (visible=False).
        self.text_edit = ft.TextField(value=text, visible=False)

        # Cria um botão de ícone (ft.IconButton) com o ícone de edição (ft.Icons.EDIT).
        # Quando clicado, ele chama o método `edit` da classe.
        self.edit_button = ft.IconButton(
            icon=ft.Icons.EDIT, on_click=self.edit)

        # Cria um botão de ícone com o ícone de salvar (ft.Icons.SAVE).
        # Esse botão é inicialmente invisível (visible=False).
        # Quando clicado, ele chama o método `save` da classe.
        self.save_button = ft.IconButton(icon=ft.Icons.SAVE, on_click=self.save,
                                         visible=False)

        # Cria um botão de ícone com o ícone de deletar (ft.Icons.DELETE).
        # Quando clicado, ele chama o método `delete` da classe.
        self.delete_button = ft.IconButton(
            icon=ft.Icons.DELETE, on_click=self.delete)

        # Define a lista de controles que serão exibidos na linha (Row).
        # A ordem dos controles define como eles serão organizados horizontalmente.
        self.controls = [
            ft.Checkbox(),  # Adiciona o próprio checkbox.
            self.text_view,  # Adiciona o widget de texto (rótulo).
            # Adiciona o campo de edição de texto (inicialmente invisível).
            self.text_edit,
            self.edit_button,  # Adiciona o botão de edição.
            # Adiciona o botão de salvar (inicialmente invisível).
            self.save_button,
            self.delete_button,  # Adiciona o botão de deletar.
        ]

    def edit(self, e):  # Método chamado quando o botão de edição é clicado.
        # Ainda não implementado. Aqui você pode adicionar a lógica para editar o texto.
        pass

    def save(self, e):  # Método chamado quando o botão de salvar é clicado.
        # Ainda não implementado. Aqui você pode adicionar a lógica para salvar o texto editado.
        pass

    def delete(self, e):  # Método chamado quando o botão de deletar é clicado.
        # Ainda não implementado. Aqui você pode adicionar a lógica para deletar o item.
        pass
