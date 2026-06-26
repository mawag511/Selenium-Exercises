from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Для смены ссылки требуется закомментировать текущую ссылку и раскомментировать ту, которую должен использовать тест
try: 
    # Первая ссылка
    link = "http://suninjuly.github.io/registration1.html"

    # Вторая ссылка
    # link = "http://suninjuly.github.io/registration2.html"

    browser = webdriver.Chrome()
    browser.get(link)

    fname = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]')
    fname.send_keys('Иван')
    lname = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
    lname.send_keys('Иванов')
    email = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')
    email.send_keys('ivanovivan@gmail.com')
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()