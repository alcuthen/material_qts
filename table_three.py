import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By




browser: object = webdriver.Chrome()

browser.get("https://www.saucedemo.com")

assert browser.find_element(By.ID, "user-name"), 'Retorno de erro'
 




