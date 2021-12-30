from programa.Controller.ImagesAndLinks import ImagesAndLinks


class ScrappingImages:

    __site = "siteDaLojaAqui"

    @classmethod
    def download_image(cls) -> None:
        # método de download de imagens
        ImagesAndLinks.image()


    @classmethod
    def cod_produto(cls) -> None:
        # método que devolve o codigo/Nome do produto
        ImagesAndLinks.cod_produto()


if __name__ == '__main__':
    pass
