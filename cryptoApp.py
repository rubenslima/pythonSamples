import os
import crypto
import flet as ft

os.system('cls' if os.name == 'nt' else 'clear')

chave_key = crypto.carregar_chave

def main(page: ft.Page):
    page.title = "Cryptos"
    page.theme_mode = ft.ThemeMode.DARK

    txt_titulo = ft.Text("Crytos:")
    criptografar = ft.TextField(
        label="Digite o nome a ser criptografado...", text_align=ft.TextAlign.LEFT
    )
    txt_chave = ft.Text(" Gerar Chave:")
    chave = ft.TextField(
        label="Digite o nome para o arquivo .key", text_align=ft.TextAlign.LEFT
    )
    
    def cadastrar(e):
        crypto.criptografar(criptografar.value, chave_key)
        print(criptografar.value)
        
    def geraChave(e):
        crypto.gerar_chave(chave.value)
    
    btn_cryto = ft.ElevatedButton("Criptografa", on_click=cadastrar)
    btn_geraChave = ft.ElevatedButton("Gerar Chave", on_click=geraChave)

    page.add(txt_titulo, criptografar, txt_chave, chave, btn_cryto, btn_geraChave)

ft.app(target=main)

