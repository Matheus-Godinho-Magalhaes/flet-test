import flet as ft
import time


def main(page: ft.Page):
    # Configurações iniciais da página da minha aplicação
    page.title = "Conversor de DOCX to PDF"
    page.window.width = 520
    page.window.height = 720
    page.theme_mode = ft.ThemeMode.DARK
    # Vai fazer com que o programa sempre fique por cima dos outros que estiverem abertos
    page.window.always_on_top = True
    page.window.maximizable = False
    page.window.resizable = False

    # Configurando o filepicker - através da documentação
    def on_dialog_result(e: ft.FilePickerResultEvent):
        if not e.files:
            return
        selected_files = e.files[0].name
        source_text.value = f"Arquivo selecionado: {selected_files}"
        page.update()

    file_picker = ft.FilePicker(on_result=on_dialog_result)
    page.overlay.append(file_picker)

    # Escolher os arquivos
    choose_file_button = ft.ElevatedButton(
        on_click=lambda _: file_picker.pick_files(allow_multiple=False),
        width=300,
        height=50,
        color="white",
        bgcolor="black",
        content=(
            ft.Text(value="Selecione o arquivo..."),
        ),

    )

    def convert_docx_to_pdf(e):
        if not result_text.value:
            result_text.value = "Escolha um arquivo word..."
            page.update()
            return

        # Caso na 2 tentativa dê certo - apenos limpo a tela
        result_text.value = ""
        progress_bar.visible = True
        page.update()

        # Escrevo a lógica do meu programa de converter aqui ou importo de outro aqui e chamo ele aqui
        try:
            print("Passei no bloco try")
            time.sleep(5)
            result_text.value = "Programa finalizado com sucesso"
        except Exception as e:
            print(f"Para no exception devido a :{e}")
        finally:
            print("Fim do programa")
            progress_bar.visible = False
            page.update()

    # Criando o botão para processar os arquivos
    convert_button = ft.ElevatedButton(
        text="Converter DOCX to PDF",
        on_click=convert_docx_to_pdf,
        width=300,
        height=50,
        color="white",
        bgcolor="black",
    )

    # Criando a barra de progresso
    progress_bar = ft.ProgressBar(color="purple", width=300, visible=False)

    source_text = ft.Text(value=" ")
    result_text = ft.Text(value=" ")

    page.add(
        ft.Container(
            width=500,
            height=670,
            bgcolor="#341F97",
            border_radius=35,
            padding=ft.padding.only(left=20, top=20, right=20, bottom=20),
            # Para um container não utilizamos o controls e sim o content que seria equivalente ao controls
            # Aqui nós fizemos por coluna pq ai vai ficar um item debaixo do outro, se fosse por linha
            # seria um item do lado do outro e não embaixo.
            content=ft.Column(
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(value="Conversor .DOCX to .PDF",
                                    size=30,
                                    color="#EB06FF",
                                    weight="bold",
                                    max_lines=1,
                                    width=400)
                        ]
                    ),
                    ft.Row(),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            choose_file_button
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            source_text
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            convert_button
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            result_text
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            progress_bar
                        ]
                    )
                ]
            )
        )
    )

    page.update()


ft.app(target=main)
