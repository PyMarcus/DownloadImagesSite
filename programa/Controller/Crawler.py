from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import multiprocessing


class Crawler:
    def __init__(self, site: str) -> None:
        self.__site: str = site

    @property
    def get_site(self):
        return self.__site


class CodNames(Crawler):
    def __init__(self, site):
        super().__init__(site)
        self.__site = super().get_site

    @staticmethod
    def intro():
        print("Aguarde")
        time.sleep(1)
        print("Acessando ao site")
        time.sleep(1)
        print("Carregando links:")
        time.sleep(1)
        print("Processando...")

    def search_codes(self):
        path: Service = Service('./chromedriver')
        driver: webdriver = webdriver.Chrome(service=path)
        driver.get(self.__site)
        valor = []
        novos_itens = []
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "fb-root")))
            time.sleep(10)
            objetos = driver.find_element(By.XPATH,
                                          "//nav[@role='navigation']//div[@id='navbar-collapse-1']//ul[@id='boxMenuLinkTop']//li[@id='produtos']//a[@title='Produtos']")
            objetos.click()  # ok clicando.Agora, acessar os links e pegar os produtos
            time.sleep(2)
            objetos1 = driver.find_element(By.XPATH,
                                           "//nav[@role='navigation']//div[@id='navbar-collapse-1']//ul[@id='boxMenuLinkTop']//li[@id='produtos']//ul[@id='menu_produtos']")
            resultado = objetos1.find_elements(By.XPATH, "//li[@class='subMenu']//a[@title='Serviços']")
            link_produtos = [x.get_attribute("href") for x in resultado]
            return link_produtos
        except NoSuchElementException as e:
            print("Erro no tempo da página")
            print(e)
        finally:
            pass


if __name__ == '__main__':
    names = CodNames("https://www.zapgrafica.com.br/loja/home")
    processo1 = multiprocessing.Process(target=CodNames.intro, args=())
    processo2 = multiprocessing.Process(target=names.search_codes, args=())
    processo2.start()
    processo1.start()
    processo1.join()
    processo2.join()
