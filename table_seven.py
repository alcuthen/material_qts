# Importação de bibliotecas nativas e criadas
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from credential import url, pwd, log_user  # biblioteca criada

# Função principal de acesso
def acess(browser):
    browser.get(url)
    title_page = browser.title

    if url == 'https://www.saucedemo.com' and title_page == 'Swag Labs':
        print("Acesso correto")

        # Mapeamento dos campos
        login_user = browser.find_element(By.XPATH, "//input[@id='user-name']")
        login_password = browser.find_element(By.XPATH, "//input[@id='password']")
        login_btn_log = browser.find_element(By.XPATH, "//input[@value='Login']")

        # Enviando dados
        login_user.send_keys(log_user)
        login_password.send_keys(pwd)

        time.sleep(2)

        login_btn_log.click()

        time.sleep(2)

        title_product = browser.find_element(By.XPATH, "//span[@data-test='title']").text

        # Asserts
        assert browser.current_url == "https://www.saucedemo.com/inventory.html", "Página interna não acessada"
        assert title_product == "Products", f"Não encontrei o título recomendado: {title_product}."

# Execução principal
if __name__ == "__main__":
    browser = webdriver.Chrome()
    try:
        acess(browser)
    except Exception as e:
        print(f"O Rauni não arrumou a rede ainda: {e}")
    finally:
        browser.quit()
