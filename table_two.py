import time 
from selenium import webdriver
from selenium.webdriver.common.by import By

browser: object = webdriver.Chrome() 

browser.get("https://www.saucedemo.com/")

# Extrair o título da página web pelo atributo title do objeto webdriver
title_page: str = browser.title
print(title_page)


if(title_page == "Swag Labs" and browser.current_url == 'https://www.saucedemo.com/'):
    print(f"A página {title_page} está correta!")

    with open('script_da_pagina.txt', "w") as script:
        script.write(browser.page_source)