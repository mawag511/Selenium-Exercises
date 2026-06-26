from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

link = "https://SunInJuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def test():
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        x_element = browser.find_element(By.ID, "input_value")
        x = x_element.text
        y = calc(x)

        browser.execute_script("window.scrollBy(0, 100);")

        answer_field = browser.find_element(By.ID, "answer")
        answer_field.send_keys(y)

        checkbox = browser.find_element(By.ID, 'robotCheckbox')
        checkbox.click()

        radio = browser.find_element(By.ID, 'robotsRule')
        radio.click()

        button = browser.find_element(By.CSS_SELECTOR, 'button[type="Submit"]')
        button.click()

    finally:
        time.sleep(10)
        browser.quit()

test()