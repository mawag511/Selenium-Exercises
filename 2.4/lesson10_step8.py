from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    price = WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )

    button = browser.find_element(By.ID, 'book')
    button.click()

    browser.execute_script("window.scrollBy(0, 100);")

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = str(math.log(abs(12*math.sin(int(x)))))

    answer_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_field.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()

finally:
    time.sleep(10)
    browser.quit()


