# Importação de bibliotecas nativas e criadas
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from credential import url, pwd, log_user #biblioteca criada.

# Criando um função chamada acess()

browser: object = webdriver.Chrome() 
browser.get(url)

def acess(browser):
       
    title_page: str = browser.title

    if url == 'https://www.saucedemo.com' and title_page == 'Swang Labs':
        print("Acesso correto")

        #browser.find_element(By.id, "user-name") ou por XPATH
        login_user: object = browser.find_element(By.XPATH, "//input[@id='user-name']")
        login_password: object = browser.find_element(By.XPATH, "//input[@id='password']")
        login_btn_log: object = browser.find_element(By.XPATH, "//input[@value='Login']")

        #Enviando dados de log, senha e submissão para os campos mapeados 
        login_user.send_keys(log_user)
        login_password.send_keys(pwd)

        time.sleep(10)

        login_btn_log.click()

        title_product: str = browser.find_element(By.XPATH, "//span[@data-test='title']")


        #assert recebe True
        #Format
        # assert COMPARAÇÃO, [ OPÇÃO DE LANÇAMENTO DE MENSAGEM ]
        assert browser.title == "https://www.saucedemo.com/inventory.html", "Página interna não acessada"
        assert title_product == "Products", "Não encontrei o título recomendado: {title_product}."

try:
    if __name__ == "__main__":
        acess(browser)

except:
    print("O Rauni não arrumou a rede ainda")

finally:
    browser.quit()