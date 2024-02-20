# pip install pytube
import os
import logging
from pytube import YouTube

os.system('cls' if os.name == 'nt' else 'clear')


def baixar_video(url):
    try:
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download()
        print("Download concluído!")
    except Exception as e:
        print("Ocorreu um erro durante o download:", str(e))
        logging.basicConfig(level=logging.INFO, filename="erro.log",
                    format="%(asctime)s - %(levelname)s modulo: %(module)s - linha %(lineno)d : %(message)s")

# Solicitar a URL do vídeo do usuário
url = input("Digite a URL do vídeo do YouTube: ")
baixar_video(url)
