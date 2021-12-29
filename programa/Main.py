from Scrapping.Scrapping import ScrappingImages


class Main:
    @staticmethod
    def start() -> None:
        ScrappingImages.download_image()


if __name__ == '__main__':
    Main.start()
    print("Concluído")
    # made by Marcus-V@Outlook.com