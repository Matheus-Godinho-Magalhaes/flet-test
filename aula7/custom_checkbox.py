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
        self.save_button = ft.IconButton(
            icon=ft.Icons.SAVE, on_click=self.save, visible=False)

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
        self.edit_button.visible = False
        self.delete_button.visible = False
        self.text_view.visible = False
        self.text_edit.visible = True
        self.save_button.visible = True
        # colocando o campor de text_Edit em foco para ser editado
        self.text_edit.focus()
        self.update()

    def save(self, e):  # Método chamado quando o botão de salvar é clicado.
        # salvando o novo valor que estava no campo text_edit para o text_view
        self.text_view.value = self.text_edit.value

        # ajustando para aparecer apenas os botões necessários
        self.edit_button.visible = True
        self.delete_button.visible = True
        self.text_view.visible = True
        self.text_edit.visible = False
        self.save_button.visible = False

        # atualizando a página para mostrar as mudanças
        self.update()

    def delete(self, e):  # Método chamado quando o botão de deletar é clicado.
        # Aqui eu apenas estou deixando a instancia invisível
        self.visible = False
        # Depois eu atualizo a página
        self.update()
