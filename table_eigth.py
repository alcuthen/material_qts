import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from credential import url



def test_ec(browser: object, url: str):

    browser.get(url)

    wait: object =  WebDriverWait(browser, 15)

    browser.find_element(By.ID,'alert').click()

    wait.until(EC.alert_is_present())
    time.sleep(2)
    




# Execução principal
if __name__ == "__main__":
    browser: object = webdriver.Chrome()

    try:
        test_ec(browser, url)
    except Exception as e:
        print(f"O erro do script é: {e}")
    finally:
        browser.quit()

