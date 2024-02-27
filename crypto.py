# pip install cryptography
from cryptography.fernet import Fernet


def gerar_chave(namekey):
    chave = Fernet.generate_key()
    with open(f"{namekey}.key", "wb") as arquivo_chave:
        arquivo_chave.write(chave)


def carregar_chave():
    with open("chave.key", "rb") as arquivo_chave:
        chave = arquivo_chave.read()
    return chave


def criptografar(texto, chave):
    f = Fernet(chave)
    texto_bytes = texto.encode("utf-8")
    texto_criptografado = f.encrypt(texto_bytes)
    return texto_criptografado.decode("utf-8")


def descriptografar(texto_criptografado, chave):
    f = Fernet(chave)
    texto_bytes = texto_criptografado.encode("utf-8")
    texto_descriptografado = f.decrypt(texto_bytes)
    return texto_descriptografado.decode("utf-8")


def criptografar_arquivo(nome_arquivo_entrada, nome_arquivo_saida, chave):
    with open(nome_arquivo_entrada, "r") as arquivo_entrada, open(
        nome_arquivo_saida, "w"
    ) as arquivo_saida:
        for linha in arquivo_entrada:
            linha_criptografada = criptografar(linha.strip(), chave)
            arquivo_saida.write(linha_criptografada + "\n")


def descriptografar_arquivo(nome_arquivo_entrada, nome_arquivo_saida, chave):
    with open(nome_arquivo_entrada, "r") as arquivo_entrada, open(
        nome_arquivo_saida, "w"
    ) as arquivo_saida:
        for linha in arquivo_entrada:
            linha_descriptografada = descriptografar(linha.strip(), chave)
            arquivo_saida.write(linha_descriptografada + "\n")


def descriptografar_linha_arquivo(nome_arquivo_entrada, chave):
    linhas_descriptografadas = []
    with open(nome_arquivo_entrada, "r") as arquivo_entrada:
        for linha in arquivo_entrada:
            linha_descriptografada = descriptografar(linha.strip(), chave)
            linhas_descriptografadas.append(linha_descriptografada)
    return linhas_descriptografadas
