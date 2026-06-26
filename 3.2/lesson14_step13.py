from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest, time

class Tests(unittest.TestCase):
    def test_registration_form_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        fname = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]')
        fname.send_keys('Mawa')
        lname = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
        lname.send_keys('G')
        email = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')
        email.send_keys('coolas@gmail.com')
        button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "In registration form 1 the welcome text is {} instead".format(welcome_text))

        time.sleep(10)
        browser.quit()

    def test_registration_form_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        fname = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]')
        fname.send_keys('Mawa')
        lname = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
        lname.send_keys('G')
        email = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')
        email.send_keys('coolas@gmail.com')
        button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "In registration form 1 the welcome text is {} instead".format(welcome_text))

        time.sleep(10)
        browser.quit()
        
if __name__ == "__main__":
    unittest.main()