import pytest, time, math
import my_secrets # Требуется создать файл my_secrets.py с LOGIN и PASSWORD переменными
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

num = [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905]
result = ''

@pytest.mark.parametrize('num', num)
def test_links(browser, num):
    global result
    browser.get(f"https://stepik.org/lesson/{num}/step/1")

    print("Link opened, login started")
    browser.implicitly_wait(5)
    try:
        login_link = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.ID, "ember519")))
        login_link.click()

        email = my_secrets.LOGIN
        password = my_secrets.PASSWORD

        email_input = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.ID, "id_login_email")))
        email_input.send_keys(email)

        password_input = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.ID, "id_login_password")))
        password_input.send_keys(password)

        login_button = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[type='submit']")))
        login_button.click()
    except Exception as e:
        print(e)

    print("Login finished")
    print("Answer calculation")

    try:
        textarea = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
        answer = math.log(int(time.time()))
        textarea.send_keys(str(answer))
        print(answer)

        time.sleep(3)
        answer_button = WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Отправить на проверку']")))
        answer_button.click()
    except Exception as e:
        print(e)

    print("Answer correction check")
    try:
        correct_sign = WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
        print(correct_sign.text)
        if correct_sign.text != "Correct!":
            result += f" {correct_sign.text}"
        time.sleep(5)
        print(result)
    except Exception as e:
        print(e)