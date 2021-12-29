import os
import time
from os import mkdir
from getpass import getuser
from .Crawler import CodNames
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import sys
from shutil import move


class ImagesAndLinks:
    @staticmethod
    def get_all() -> None:
        names: str = CodNames("https://www.zapgrafica.com.br/loja/home")
        CodNames.intro()
        links = names.search_codes()
        codigos: list = []
        imagens: list = []
        for link in links:
            url = requests.get(link)
            bs = BeautifulSoup(url.content, 'html.parser')
            # codigo de produtoss
            valor1 = bs.find_all("div", {"class":"box-info-servico"})
            valor2 = bs.find_all("img", {"alt":"Adicionar ao Carrinho"})
            codigos.append(valor1)
            imagens.append(valor2)
        return codigos, imagens

    @staticmethod
    def cod_produto() -> list:
        codigos: list = ImagesAndLinks.get_all()[0]
        codigo_armazenar: list = []
        print("Capturando os códigos dos produtos")
        for listas in codigos:
            for texto in listas:
                if str(texto)[64:73] not in codigo_armazenar:
                    text = str(texto)[64:73].replace(">", "")
                    novo = text.replace("<", "")
                    outro = novo.replace("/", "")
                    #print(outro)
                    codigo_armazenar.append(outro)
        #print(len(codigo_armazenar))
        return codigo_armazenar

    @staticmethod
    def image() -> None:
        images: list = ImagesAndLinks.get_all()[1]
        links: list = []
        print("Baixando imagens")
        for image in images:
            for i in image:
                if "src" in i.attrs:
                    if i["src"] not in links:
                        links.append(i["src"])
        #print(len(links))
        codigos: list = ImagesAndLinks.cod_produto()
        dicionario_img_cod: dict = dict(zip(codigos, links))
        caminho: str = sys.argv[0]
        usuario: str = getuser()
        if "ImagesZap" not in os.listdir(f"C:\\Users\\{usuario}\\"):
            mkdir(f"C:\\Users\\{usuario}\\ImagesZap\\")
            time.sleep(1)
            for k, v in dicionario_img_cod.items():
                if v not in os.listdir(f"C:\\Users\\{usuario}\\ImagesZap\\"):
                    urlretrieve(v, f"{str(k)}.jpg")
                    time.sleep(1)
                    move(f"{str(k)}.jpg", f"C:\\Users\\{usuario}\\ImagesZap\\")
        else:
            for k, v in dicionario_img_cod.items():
                if v not in os.listdir(f"C:\\Users\\{usuario}\\ImagesZap\\"):
                    urlretrieve(v, f"{str(k)}.jpg")
                    time.sleep(1)
                    move(f"{str(k)}.jpg", f"C:\\Users\\{usuario}\\ImagesZap\\")


if __name__ == '__main__':
    #ImagesAndLinks.get_all()
    #ImagesAndLinks.cod_produto()
    ImagesAndLinks.image()
