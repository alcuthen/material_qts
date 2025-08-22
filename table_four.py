import time 
from selenium import webdriver
from selenium.webdriver.common.by import By


browser: object = webdriver.Chrome() 

browser.get("https://demo.applitools.com/")

log_user = browser.find_element(By.ID,"username")
password_user = browser.find_element(By.ID,"password")
select_remember_user = browser.find_element(By.XPATH,"//input[@class='form-check-input']")

time.sleep(3)
assert log_user.is_displayed(), "O input de log não está disponível"

assert password_user.is_enabled(), "O input de senha não está disponível"
assert not select_remember_user.is_selected(), "A opção lembrar de log não está marcada"



