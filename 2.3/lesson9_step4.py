from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

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


