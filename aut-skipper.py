import time
import pyautogui
import keyboard
import os
import requests
import tempfile
import atexit
from PIL import Image

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def cabeçalho_script():
    print("\033[1;34m")
    print(r"  ____            _       _    ")
    print(r" / ___|  ___ _ __(_)_ __ | |_  ")
    print(r" \___ \ / __| '__| | '_ \| __| ")
    print(r"  ___) | (__| |  | | |_) | |_  ")
    print(r" |____/ \___|_|  |_| .__/ \__| ")
    print(r"                   |_|                        ")
    print("\033[0m")
    print("Criado por Viajante47, todos os direitos reservados!\n")

def baixar_e_salvar_imagem(url, nome_arquivo):
    resposta = requests.get(url)
    caminho_arquivo = os.path.join(tempfile.gettempdir(), nome_arquivo)
    with open(caminho_arquivo, 'wb') as arquivo:
        arquivo.write(resposta.content)
    return caminho_arquivo

def configurar():
    print("Iniciando os componentes do script...")
    urls_imagens = {
        'pularopcrunch.png': 'https://i.ibb.co/6RWy739/pularopcrunch.png',
        'pularrecapcrunchy.png': 'https://i.ibb.co/khMtPrh/pularrecapcrunchy.png',
        'pularendcrunch.png': 'https://i.ibb.co/VjL9kcQ/pularendcrunch.png',
        'pularopnetflix.png': 'https://i.ibb.co/Y7svGRL/pularopnetflix.png',
        'amazonprimeanuncio.png': 'https://i.ibb.co/RDVykmm/amazonprimeanuncio.png',
        'pularopamazonprime.png': 'https://i.ibb.co/NYkxGmM/pularopamazonprime.png',
        'pularopdisney.png': 'https://i.ibb.co/kQC01yj/pularopdisney.png',
        'pularanuncioyt.png': 'https://i.ibb.co/Cb9ck7V/pularanuncioyt.png'
    }
    caminhos_imagens = {}
    for nome, url in urls_imagens.items():
        caminhos_imagens[nome] = baixar_e_salvar_imagem(url, nome)
    return caminhos_imagens

def remover_arquivos_temporarios(caminhos_imagens):
    for caminho in caminhos_imagens.values():
        try:
            os.remove(caminho)
        except OSError as e:
            print(f"Erro ao remover o arquivo temporário {caminho}: {e}")

def clicar_botao(caminho_imagem):
    try:
        x, y = pyautogui.locateCenterOnScreen(caminho_imagem, confidence=0.8)
        if x and y:
            pyautogui.click(x, y)
    except Exception as e:
        pass

def escolher_servico():
    print("Escolha o serviço de streaming:")
    print("1. Crunchyroll")
    print("2. Netflix")
    print("3. Amazon Prime Video")
    print("4. Disney Plus")
    print("5. YouTube")
    escolha = input("Digite o número do serviço: ")
    return escolha

def pular_abertura_crunchyroll(caminhos_imagens):
    clicar_botao(caminhos_imagens['pularopcrunch.png'])
    clicar_botao(caminhos_imagens['pularrecapcrunchy.png'])
    clicar_botao(caminhos_imagens['pularendcrunch.png'])

def pular_abertura_netflix(caminhos_imagens):
    clicar_botao(caminhos_imagens['pularopnetflix.png'])

def pular_anuncio_prime_video(caminhos_imagens):
    clicar_botao(caminhos_imagens['amazonprimeanuncio.png'])
    clicar_botao(caminhos_imagens['pularopamazonprime.png'])

def pular_abertura_disney_plus(caminhos_imagens):
    clicar_botao(caminhos_imagens['pularopdisney.png'])

def pular_anuncio_youtube(caminhos_imagens):
    clicar_botao(caminhos_imagens['pularanuncioyt.png'])

def main():
    limpar_terminal()
    cabeçalho_script()
    caminhos_imagens = configurar()
    atexit.register(remover_arquivos_temporarios, caminhos_imagens)
    
    while True:
        limpar_terminal()
        cabeçalho_script()
        escolha = escolher_servico()
        print("Script iniciando...")
        while True:
            if keyboard.is_pressed('q'):
                break
            if escolha == '1':
                pular_abertura_crunchyroll(caminhos_imagens)
            elif escolha == '2':
                pular_abertura_netflix(caminhos_imagens)
            elif escolha == '3':
                pular_anuncio_prime_video(caminhos_imagens)
            elif escolha == '4':
                pular_abertura_disney_plus(caminhos_imagens)
            elif escolha == '5':
                pular_anuncio_youtube(caminhos_imagens)
            else:
                print("Escolha inválida. Por favor, escolha novamente.")
                break
            time.sleep(0.3)
            print("Script rodando... (pressione 'q' para voltar)", end='\r')

if __name__ == "__main__":
    main()
