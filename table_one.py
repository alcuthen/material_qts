# Importação de bibliotecas no script
import time
from selenium import webdriver

# Cria uma instância de um objeto webdriver, utilizado para acessar e explorar páginas web
browser: object = webdriver.Chrome()

# Acessar a página do google
browser.get("https://www.google.com")

# Extrair o título da página web pelo atributo title do objeto webdriver
title_page: str = browser.title

# Maximizar a página web
browser.fullscreen_window()
time.sleep(2)

# Abrir outra página
browser.get("https://www.ibm.com")
time.sleep(2)

# Retornar a página anterior
browser.back()
