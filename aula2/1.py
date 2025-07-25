import flet as ft


def main(page: ft.Page):

    # Primeiro eu crio as variáveis, nesse caso eu criei a variável texto,
    # depois eu defino o que essa variável vai receber
    texto = ft.Text(value="Bem vindo ao app Godinho World!!")
    texto2 = ft.Text(value="Acrescentando mais uma linha de texto")

    # Depois eu adiciono essa minha variável na página
    page.add(texto)
    page.add(texto2)


ft.app(target=main)
