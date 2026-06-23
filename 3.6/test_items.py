import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_btn_presence(browser):
    browser.get(url)
    time.sleep(30)

    add_to_basket_selector = (By.CSS_SELECTOR, "#add_to_basket_form button[type='submit']")
    add_to_basket_button = WebDriverWait(browser, 15).until(EC.presence_of_element_located(add_to_basket_selector))

    assert add_to_basket_button is not None, "'Add to basket' button is not visible"