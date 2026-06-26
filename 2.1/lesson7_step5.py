from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

link = "https://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def test():
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
        x = x_element.text
        y = calc(x)

        answer_field = browser.find_element(By.CSS_SELECTOR, "#answer")
        answer_field.send_keys(y)

        checkbox = browser.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')
        checkbox.click()

        radio = browser.find_element(By.CSS_SELECTOR, 'input[value="robots"]')
        radio.click()

        button = browser.find_element(By.CSS_SELECTOR, 'button')
        button.click()

    finally:
        time.sleep(10)
        browser.quit()

test()