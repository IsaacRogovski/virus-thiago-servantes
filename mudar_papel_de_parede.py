import ctypes
import os
import urllib.request
from PIL import Image
import io

def baixar_imagem(url, nome_arquivo):
    """Baixa a imagem da URL e salva localmente com o nome fornecido."""
    try:
        # Fazer download da imagem
        with urllib.request.urlopen(url) as response:
            image_data = response.read()

        # Salvar a imagem localmente
        caminho_imagem = os.path.join(os.getcwd(), nome_arquivo)
        with open(caminho_imagem, 'wb') as f:
            f.write(image_data)
        print(f"Imagem baixada e salva em: {caminho_imagem}")
        return caminho_imagem
    except Exception as e:
        print(f"Erro ao baixar a imagem: {e}")
        return None

def mudar_papel_de_parede(caminho_imagem):
    """Define a imagem como papel de parede."""
    if not os.path.isfile(caminho_imagem):
        print(f"Arquivo não encontrado: {caminho_imagem}")
        return

    # Define a imagem como papel de parede (estilo 2 = tela cheia)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, caminho_imagem, 3)
    print(f"Papel de parede alterado para: {caminho_imagem}")

# URL da imagem na internet
url_imagem = "https://s2-g1.glbimg.com/71zxSCRIFqH_YmGsZHa_Pp0DPDU=/0x0:6558x5886/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2020/w/M/dPe7LwQ9ewnBmBjigVDA/tiago-cervantes-candidato-de-itanhaem.jpg"

# Nome do arquivo local para salvar a imagem
nome_arquivo_local = "imagem_temporaria.jpg"

# Baixar a imagem da internet
caminho_da_imagem = baixar_imagem(url_imagem, nome_arquivo_local)

# Se a imagem foi baixada com sucesso, alterar o papel de parede
if caminho_da_imagem:
    mudar_papel_de_parede(caminho_da_imagem)

