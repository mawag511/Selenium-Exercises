from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    el1 = browser.find_element(By.ID, "num1")
    el2 = browser.find_element(By.ID, "num2")
    result = int(el1.text) + int(el2.text)

    answer_field = Select(browser.find_element(By.ID, "dropdown"))
    answer_field.select_by_value(str(result)) 

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
