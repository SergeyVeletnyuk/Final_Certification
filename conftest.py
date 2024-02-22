import pytest
import requests
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    browserr = testdata['browser']


# Опции только для хрома
# options = webdriver.ChromeOptions()


@pytest.fixture()  # @pytest.fixture(scope='session') Сразу для всех тестов без закрытия сайта
def browser():
    if browserr == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def get_title_font_size():
    return "32px"


@pytest.fixture()
def test_login():
    response = requests.post(url="https://test-stand.gb.ru/gateway/login",
                             data={'username': testdata['login'], 'password': testdata['passwd']})

    # if response.status_code == 200:
    token = response.json()['token']
    return token
