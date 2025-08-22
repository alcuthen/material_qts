from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def add_assert(func):
    def wrapper(*args, **kwargs):
        browser = func(*args, **kwargs)
        try:
            log_user = browser.find_element(By.ID, "username")
            assert log_user.is_displayed(), "O input de log não está disponível"
            print("Elemento 'username' encontrado e visível.\033[92m✔\033[0m")
            return browser, log_user
        except NoSuchElementException:
            print("Elemento 'username' não encontrado. \033[0;31mX\033[0m")
            browser.quit()
            raise 
    return wrapper

@add_assert
def test(url: str):
    browser: webdriver.Chrome = webdriver.Chrome()
    browser.get(url)
    return browser

if __name__ == "__main__":
    try:
        browser, log_user = test("https://demo.applitools.com")
    finally:
        if 'browser' in locals() and browser.service.is_connectable():
            browser.quit()