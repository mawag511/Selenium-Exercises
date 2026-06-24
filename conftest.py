import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Set the language for tests")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print("\nStart Chrome Browser...")

    options = Options()
    # options.add_argument('headless')
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)

    yield browser
    print("\nQuit Chrome Browser...")
    browser.quit()