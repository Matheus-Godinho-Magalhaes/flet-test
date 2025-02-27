# Esqueleto principal para criar um programa no Flet

import flet as ft


def main(page: ft.Page):
    # Aqui eu configurei um elemento de texto
    texto = ft.Text(value="Bem vindo ao app Godinho World!")
    # depois eu adicionei o elemento de texto na página
    page.add(texto)


ft.app(target=main)

# Para rodar o programa, execute o comando:
# flet run aula1.py
