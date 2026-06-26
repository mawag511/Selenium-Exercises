from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    fname = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    fname.send_keys('Mawa')
    lname = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
    lname.send_keys('G')
    email = browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
    email.send_keys('coolasf@gmail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__)) 
    file_path = os.path.join(current_dir, 'file.txt') 
    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys(os.path.abspath(os.path.dirname(__file__)))

    submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()


